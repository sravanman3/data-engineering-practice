def transform_sales_data(sales_data):
    error_list = []
    transformed_list = []
    total_records = len(sales_data)
    success_count = 0
    error_count = 0
    for sale in sales_data:
        try:
            sale_amount = float(sale["amount"])
            transformed_record = {
                "txn_id" : sale["txn_id"].strip(),
                "customer" : sale["customer"].strip(),
                "product_type" : sale["product_type"].strip(),
                "amount" : sale_amount,
                "tax" : round(sale_amount * 0.18,2),
                "handling_fee" : 100 if sale["product_type"].lower() == "electronics" else 0
            }
            transformed_list.append(transformed_record)
            success_count += 1
        except (ValueError, KeyError) as e:
            error_count += 1
            error_list.append(
                {
                    "record" : sale,
                    "error" : str(e)
                }
            )
    failure_rate = (error_count /total_records) * 100 if total_records > 0 else 0
    return {
        "valid" : transformed_list,
        "errors" : error_list,
        "total" : total_records,
        "success" : success_count,
        "failed" : error_count,
        "failure_rate" : failure_rate

    }


# transform_sales_data([{'txn_id': '1', 'customer': 'A', 'product_type': 'Electronics', 'amount': '100'}, {'txn_id': '2', 'customer': 'B', 'product_type': 'SALE', 'amount': '-50'}, {'txn_id': '3', 'customer': 'A', 'product_type': 'REFUND', 'amount': '-20'}])

