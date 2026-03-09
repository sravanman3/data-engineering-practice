import csv

def extract_sales(file_name) -> dict:
    result = {
        "data": [],
        "errors": [],
        "total_records": 0,
        "invalid_records": 0,
        "valid_records": 0
    }
    error_list = []
    valid_txns_list = []
    total_record_count = 0
    valid_txns_count = 0
    error_txn_count = 0
    with open(file_name, newline='') as sales_file:
        reader = csv.DictReader(sales_file)

        fieldnames = reader.fieldnames

        if fieldnames is None:
            result["errors"] = ["Empty file received"]
            return result

        required_fields = ["txn_id", "customer", "product_type", "amount"]

        for col in required_fields:
            if col not in fieldnames:
                result["errors"].append(f"Required field {col} is missing")
                return result

        seen_txns = set()

        for row_number,row in enumerate(reader,start=2):

            error_dict={}

            if not any(row.values()):
                continue
            total_record_count += 1

            missing_fields = []
            for field in required_fields:
                if not row.get(field,"").strip():
                    missing_fields.append(field)

            txn_id = row.get("txn_id","").strip()



            if missing_fields:
                error_dict = {
                    "row_number" :row_number,
                    "row" : row,
                    "error" : f"Missing columns {','.join(missing_fields)} "
                }
                error_txn_count += 1
                error_list.append(error_dict)
            elif txn_id in seen_txns:
                error_dict = {
                    "row_number" : row_number,
                    "row" : row,
                    "error" : "duplicate txn",
                }
                error_txn_count += 1
                error_list.append(error_dict)
            else:
                clean_row = {col: row.get(col,"").strip() for col in required_fields}
                valid_txns_count += 1
                valid_txns_list.append(clean_row)
                seen_txns.add(txn_id)

        result["total_records"] = total_record_count
        result["invalid_records"] = error_txn_count
        result["valid_records"] = valid_txns_count
        result["errors"] = error_list
        result["data"] = valid_txns_list


        return result
