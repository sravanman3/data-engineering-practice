import csv

# def read_sales_file(file_name):
#     list_of_txns = []
#     with open(file_name, newline='') as txn_data:
#         sales_data = csv.reader(txn_data)
#         next(sales_data)  ## skip header if present
#         for row in sales_data:
#             sales_dict = {
#                 "txn_id": row[0],
#                 "customer": row[1],
#                 "product_type": row[2],
#                 "amount": row[3]
#             }
#
#             list_of_txns.append(sales_dict)
#
#     return list_of_txns

def read_sales_data(file_name):
    txns_list = []
    try:
        with open(file_name, newline='') as sales_data:
            sales_reader = csv.DictReader(sales_data)
            for row in sales_reader:
                txns_list.append(row)

        print(f"Total number of records extracted: {len(txns_list)}")
        return txns_list

    except FileNotFoundError:
        print("File not available")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

