def aggregate_sales(valid_txns):

    rev_per_customer = {}
    rev_per_product = {}
    order_per_product = {}
    total_revenue = 0

    for txn_id,customer,product,amount in valid_txns:
        rev_per_customer[customer] = rev_per_customer.get(customer,0) + amount
        rev_per_product[product] = rev_per_product.get(product,0) + amount
        total_revenue += amount
        order_per_product[product] = order_per_product.get(product,0) + 1

    top_customers = sorted(rev_per_customer.items(), key = lambda x:x[1], reverse = True)[:3]
    avg_order_value = total_revenue / len(valid_txns)
    most_popular_product = max(order_per_product.items(), key= lambda x:x[1])

    print(rev_per_product)

    return rev_per_customer,rev_per_product,top_customers,avg_order_value,most_popular_product
