import datetime
import os
import glob

from sales_pipeline.extract import extract as extract
from sales_pipeline.transform import transform_sales as transform
from sales_pipeline.load import load_errors as load_errors, load as load

from sales_pipeline.utils.logger import logger

import json

def load_config():
    with open("config/config.json", "r") as f:
        return json.load(f)

def generate_run_id():
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    files = glob.glob(os.path.join(reports_dir, f"pipeline_report_{today}_*.json"))

    if not files:
        return f"{today}_001"

    run_numbers = []

    for file in files:
        name = os.path.basename(file)
        run_num = name.split("_")[-1].replace(".json", "")
        run_numbers.append(int(run_num))

    next_run = max(run_numbers)+1
    return f"{today}_{str(next_run).zfill(3)}"

def update_metrics(report, metric_file_name="reports/data_quality_metrics.json"):
    default_metrics = {
            "total_pipeline_runs": 0,
            "total_records_processed": 0,
            "total_errors": 0,
            "average_error_rate": 0
        }
    metrics = default_metrics.copy()
    if os.path.exists(metric_file_name):
        try:
            with open(metric_file_name) as f:
                data = f.read().strip()
                if data:
                    metrics = json.loads(data)
        except json.JSONDecodeError:
            logger.warning("Metrics file corrupted, reinitializing metrics")


    metrics["total_pipeline_runs"] += 1
    records = report.get("total_records",0)
    errors = (report.get("invalid_records",0) + report.get("transform_invalid",0))

    metrics["total_records_processed"] += records
    metrics["total_errors"] += errors

    if metrics["total_records_processed"] > 0:
        metrics["average_error_rate"] = round((metrics["total_errors"] / metrics["total_records_processed"]),2)

    metrics["last_run_status"] = report.get("status")

    with open(metric_file_name,"w") as f:
        json.dump(metrics,f,indent=4)

def main():
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info("Pipeline started")
    pipeline_report = {}
    status = "Success"
    error_rate = 0
    try:
        config = load_config()
        logger.info("config loaded")
        extract_result = extract.extract_sales(config["input_file"])
        pipeline_report = {
            "total_records": extract_result.get("total_records"),
            "valid_records": extract_result.get("valid_records"),
            "extract_errors": extract_result.get("extract_errors")
        }

        trans_result = transform.transform_sales(extract_result["data"], config)
        pipeline_report["transform_valid" ] = len(trans_result["data"])
        pipeline_report["transform_errors"] = len(trans_result["errors"])

        if pipeline_report["total_records"] == 0:
            raise Exception("No records found in file")

        total_errors = pipeline_report["extract_errors"] + pipeline_report["transform_errors"]
        error_rate =  total_errors/pipeline_report["total_records"]

        if error_rate > config["error_threshold"]:
            raise Exception("error rate exceeded threshold")

        load.load_sales(trans_result["data"],config["output_file"])
        load_errors.load_errors(trans_result["errors"], config["error_file"])
    except Exception as e:
        logger.error(f"error occurred in pipeline execution: {str(e)}")
        status = "Failed"
        pipeline_report["error_message"] = str(e)
    finally:
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pipeline_report["status"] = status
        pipeline_report["start_time"] = start_time
        pipeline_report["end_time"] = end_time
        pipeline_report["error_rate"] = error_rate
        batch_date = datetime.datetime.now().strftime("%Y-%m-%d")

        pipeline_report["batch_date"] = batch_date
        pipeline_report["records_processed"] = pipeline_report.get("transform_valid", 0)

        pipeline_run_id = generate_run_id()
        pipeline_report["pipeline_run_id"] = pipeline_run_id
        reports_dir = "reports"
        os.makedirs(reports_dir, exist_ok=True)
        pipeline_report_file = os.path.join(reports_dir,f"pipeline_report_{pipeline_run_id}.json")

        with open(pipeline_report_file,"w") as f:
            json.dump(pipeline_report,f,indent=4)

        update_metrics(pipeline_report)
        logger.info(f"Pipeline completed with status: {status}")


if __name__ == "__main__":
    main()