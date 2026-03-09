
def transform_sales(sales):
    result = {
        "data" : [],
        "errors" : []
    }

    error_list=[]
    allowed_products = {"Electronics","Grocery","Clothing"}
    tax_rates = {"Electronics": 0.18, "Clothing" : 0.05 , "Grocery" : 0}
    valid_txns = []
    for row in sales:
        product_type = row.get("product_type","").strip().title()
        if product_type not in allowed_products:
            error_list.append({
                "txn_id": row.get("txn_id").strip(),
                "customer": row.get("customer").strip(),
                "product_type": product_type,
                "amount": row.get("amount").strip(),
                "error": f"Invalid Product Type: {row['product_type']}"
            })
            continue

        try:
            amount_float = float(row.get("amount").strip())
        except ValueError:
            error_list.append({
                "txn_id": row.get("txn_id").strip(),
                "customer": row.get("customer").strip(),
                "product_type": row["product_type"].strip(),
                "amount": row.get("amount").strip(),
                "error": f"Invalid amount: {row.get('amount')}"
            })
            continue

        if amount_float <= 0:
            error_list.append({
                "txn_id" : row.get("txn_id").strip(),
                "customer" : row.get("customer").strip(),
                "product_type" : row.get("product_type").strip(),
                "amount" : row.get("amount").strip(),
                "error" : f"Invalid amount: {row.get('amount')}"
            })
            # error_list.append(error_dict)
            continue

        tax_amount = round(amount_float * tax_rates[product_type],2)
        transformed_row = {
            "txn_id" : row.get("txn_id").strip(),
            "customer" : row.get("customer").strip(),
            "product_type" : product_type,
            "amount" : amount_float,
            "tax" : tax_amount,
        }
        valid_txns.append(transformed_row)

    result["data"] = valid_txns
    result["errors"] = error_list

    return result


data = [{'txn_id': 'T1', 'customer': 'Alice', 'product_type': 'electronics', 'amount': '100'}, {'txn_id': 'T2', 'customer': 'Bob', 'product_type': 'Grocery', 'amount': 'abc'},
        {'txn_id': 'T3', 'customer': 'Joe', 'product_type': 'Electronics', 'amount': '-10'},
        {'txn_id': 'T4', 'customer': 'Max', 'product_type': 'Clothing', 'amount': '10'}]
print(transform_sales(data))