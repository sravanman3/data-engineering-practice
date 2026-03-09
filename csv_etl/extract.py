import csv


def extract_sales(file_name) -> dict:
    valid_txns_list = []
    error_list = []
    valid_record_count =0
    total_record_count =0
    result = {
        "data": [],
        "errors": [],
        "total_records": 0,
        "invalid_records": 0
    }
    try:
        with open(file_name, newline='') as sales_data:
            sales_reader = csv.DictReader(sales_data)
            fieldnames = sales_reader.fieldnames
            if fieldnames is None:
                return {
                    "data": [],
                    "errors": ["Empty File Received"],
                    "total_records": 0,
                    "invalid_records": 0
                }
            required_columns = ["txn_id", "customer", "product_type","amount"]
            for col in required_columns:
                if col not in fieldnames:
                    return {
                        "data": [],
                        "errors": ["Mandatory columns missing " + col],
                        "total_records": 0,
                        "invalid_records": 0
                    }

            for row_number,row in enumerate(sales_reader, start=2):
                error_dict = {}

                if not any(row.values()):
                    continue
                total_record_count += 1

                missing_fields = []
                for field in required_columns:
                    if not row.get(field,"").strip():
                        missing_fields.append(field)

                if missing_fields:
                    error_dict = {
                        "row_number" : row_number,
                        "row" : row,
                        "error" : f"missing columns {','.join(missing_fields)}"
                    }
                    error_list.append(error_dict)
                else:
                    valid_record_count += 1
                    valid_txns_list.append(row)


            return {
                "data": valid_txns_list,
                "errors": error_list,
                "total_records": total_record_count,
                "valid_records": valid_record_count,
                "invalid_records": len(error_list)
            }

    except FileNotFoundError:
        return result

print(extract_sales("demo.csv"))