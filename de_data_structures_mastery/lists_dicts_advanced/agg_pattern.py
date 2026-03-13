sales = [
 ("T1","Alice","electronics",100),
 ("T2","Bob","grocery",200),
 ("T3","Alice","grocery",50),
 ("T4","Bob","electronics",150),
 ("T5","Alice","electronics",200)
]

customer_sales= {}
# for sale in sales:
#     if sale[1] not in customer_sales:
#         customer_sales[sale[1]] = sale[3]
#     else:
#         customer_sales[sale[1]] += sale[3]

# for txn_id,customer,product_type,amount in sales:
#     if customer not in customer_sales:
#         customer_sales[customer] = amount
#     else:
#         customer_sales[customer] += amount

for txn_id,customer,product_type,amount in sales:
    customer_sales[customer] = customer_sales.get(customer,0) + amount

print(customer_sales)
