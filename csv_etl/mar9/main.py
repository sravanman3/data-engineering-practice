import extract as extract
from sales_pipeline.transform import transform_sales as transform
from sales_pipeline.load import load_errors as load_errors, load as load

import json

def main():
    extract_result = extract.extract_sales("dup_sales.csv")
    pipeline_report = {
        "total_records": extract_result.get("total_records"),
        "valid_records": extract_result.get("valid_records"),
        "invalid_records": extract_result.get("invalid_records")
    }

    trans_result = transform.transform_sales(extract_result["data"])
    pipeline_report["transform_valid" ] = len(trans_result["data"])
    pipeline_report["transform_invalid"] = len(trans_result["errors"])
    load.load_sales(trans_result["data"])
    load_errors.load_errors(trans_result["errors"], "error_sales.csv")

    with open("pipeline_report.json","w") as f:
        json.dump(pipeline_report,f,indent=4)

if __name__ == "__main__":
    main()