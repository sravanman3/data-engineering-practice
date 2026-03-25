import csv

from random_data_generator import random_generator
from validator import validate_sales
from stream_aggregator import Aggregator
import time

def main():
    start_time = time.time()
    no_of_transactions = 1000000
    sales_streaming = random_generator(no_of_transactions)

    validated_stream = validate_sales(sales_streaming)

    with open("valid.csv", "w", newline="") as valid_file,open("error.csv", "w", newline="") as error_file:
        valid_writer = csv.writer(valid_file)
        valid_writer.writerow(["txn_id", "Customer", "Product", "Amount"])

        error_writer = csv.DictWriter(error_file,
                                      fieldnames=["txn_id", "customer", "error_type", "error_msg", "timestamp"])
        error_writer.writeheader()

        valid_count = 0
        error_count = 0

        aggregator = Aggregator()

        for status, record in validated_stream:

            if status == "valid":
                aggregator.process(record)
                valid_writer.writerow(record)
                valid_count += 1

            else:
                error_writer.writerow(record)
                error_count += 1

    total_transactions = no_of_transactions

    avg_order_value = (
        aggregator.total_amount / aggregator.total_count if aggregator.total_count else 0
    )

    top_customers = sorted(aggregator.rev_per_customer.items(), key=lambda x:x[1],reverse=True)[:3]
    most_popular_product = max(
        aggregator.product_count.items(),
        key=lambda x: x[1]
    )

    with open("summary_report.txt", "w") as file:
        file.write("ETL SUMMARY REPORT\n")
        file.write("----------------------------\n")

        file.write(f"Total Transactions: {total_transactions}\n")
        file.write(f"Valid Transactions: {valid_count}\n")
        file.write(f"Error Transactions: {error_count}\n\n")

        file.write(f"Average Order Value: {round(avg_order_value, 2)}\n\n")

        file.write("Top 3 Customers by Revenue\n")
        file.write("----------------------------\n")
        for cust, revenue in top_customers:
            file.write(f"{cust}: {round(revenue, 2)}\n")

        file.write("\nRevenue Per Product\n")
        file.write("----------------------------\n")
        for prod, revenue in aggregator.rev_per_product.items():
            file.write(f"{prod}: {round(revenue, 2)}\n")

        file.write("\nMost Popular Product\n")
        file.write(f"{most_popular_product[0]}: {most_popular_product[1]}\n")

    # Step 8: Performance Metrics
    end_time = time.time()
    run_time = end_time - start_time
    records_per_second = round(no_of_transactions / run_time, 2)

    print("ETL JOB COMPLETED\n")
    print(f"Total Transactions: {total_transactions}")
    print(f"Valid Transactions: {valid_count}")
    print(f"Error Transactions: {error_count}\n")
    print(f"Avg Order Value: {avg_order_value}")
    print(f"Top Customers: {top_customers}")
    print(f"Run time: {run_time}")
    print(f"Records per second: {records_per_second}")
    print(f"Most popular product: {most_popular_product}")

    # Close files
    valid_file.close()
    error_file.close()

if __name__ == "__main__":
    main()