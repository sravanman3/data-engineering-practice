import csv

def load_errors(records, output_file):
    with open(output_file, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= ["txn_id","customer","product_type","amount","error"])
        writer.writeheader()
        writer.writerows(records)