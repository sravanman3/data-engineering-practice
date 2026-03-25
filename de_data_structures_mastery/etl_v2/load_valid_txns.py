import csv

def load_valid_txns(filename,valid_txns):
    with open(filename,"w",newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["txn_id","Customer","Product","Amount"])
        writer.writerows(valid_txns)