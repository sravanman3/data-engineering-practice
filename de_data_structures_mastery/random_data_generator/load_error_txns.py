import csv

def load_error_txns(filename,error_txns):
    with open(filename,"w",newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["txn_id","customer","error_type","error_msg","timestamp"]
        )
        writer.writeheader()
        writer.writerows(error_txns)
