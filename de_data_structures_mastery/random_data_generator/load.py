import csv

def load_txns(filename,valid_txns):
    with open(filename,"w",newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["txn_id","customer","product","amount"])
        csvwriter.writerows(valid_txns)
