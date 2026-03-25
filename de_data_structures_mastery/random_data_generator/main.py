from validation import validate_txns
from random_10k import generate_random_sales
from load import load_txns
from load_error_txns import load_error_txns

from datetime import datetime

def main():
    start_time = datetime.now()

    # sales = generate_random_sales(500000)
    # valid_txns,error_txns = validate_txns(sales)

    sales_stream = generate_random_sales(500000)
    valid_txns, error_txns = validate_txns(sales_stream)

    load_txns("valid_transactions.csv",valid_txns)
    load_error_txns("error_logs.csv",error_txns)

    end_time = datetime.now()
    # total_records = len(sales)
    total_records = len(valid_txns) + len(error_txns)
    runtime_seconds = (end_time - start_time).total_seconds()

    print(f"Total Run time:  {runtime_seconds}")
    # print(f"Total Transactions:  {total_records}")
    print(f"Total Valid Transactions:  {len(valid_txns)}")
    print(f"Total Errors:  {len(error_txns)}")

    records_per_second = total_records / runtime_seconds
    print("Record per second: ",records_per_second)

if __name__ == "__main__":
    main()
