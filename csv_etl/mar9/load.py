import csv

def load_sales(records,output_file="trans_sales.csv"):
    if not records:
        print("No records to load")
        return
    with open(output_file, 'w',newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["txn_id", "customer", "product_type", "amount", "tax"])
        writer.writeheader()
        writer.writerows(records)