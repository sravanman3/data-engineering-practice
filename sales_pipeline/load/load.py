from sales_pipeline.utils.logger import logger
import csv

def load_sales(records,output_file):
    if not records:
        logger.info("No sales records found")
        return
    with open(output_file, 'w',newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["txn_id", "customer", "product_type", "amount", "tax"])
        writer.writeheader()
        writer.writerows(records)