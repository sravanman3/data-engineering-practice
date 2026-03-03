import csv

import extract as extract_data
import transform as transform_data

def etl_execute():
    txns_list = extract_data.read_sales_data("sales_data.csv")
    trans_formed_dict = transform_data.transform_sales_data(txns_list)

    print(f"Processing info: {trans_formed_dict}")

    failure_rate = trans_formed_dict["failure_rate"]
    error_records = trans_formed_dict["errors"]
    if failure_rate > 5.0:
        print("BATCH FAILED")
        with open("error_records.csv", "w", newline="") as error_file:
            fieldnames = ["record", "error"]

            writer = csv.DictWriter(error_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(error_records)

    else:
        print("BATCH SUCCEEDED")
        valid_records = trans_formed_dict["valid"]

        print("Batch Summary:")
        print(f"Total records: {len(txns_list)}")
        print(f"Successful records: {len(valid_records)}")
        print(f"Failed records: {len(error_records)}")
        print(f"Failure rate: {failure_rate}")

        with open("transformed_data.csv", "w", newline="") as write_file:
            fieldnames = ["txn_id", "customer", "product_type", "amount", "tax", "handling_fee"]

            writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_records)



etl_execute()
