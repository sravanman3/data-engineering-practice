
from sales_pipeline.utils.logger import logger

def transform_sales(sales, config):

    result = {
        "data" : [],
        "errors" : []
    }

    error_list=[]
    allowed_products = config["allowed_products"]
    tax_rates = config["tax_rates"]
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

    logger.info(f"total valid txns in this run : {len(valid_txns)}")
    logger.info(f"total error txns in this run : {len(error_list)}")

    result["data"] = valid_txns
    result["errors"] = error_list

    return result


