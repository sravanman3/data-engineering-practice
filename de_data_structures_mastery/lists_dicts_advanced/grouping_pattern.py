sales = [
 ("T1","Alice","electronics",100),
 ("T2","Bob","grocery",200),
 ("T3","Alice","grocery",50),
 ("T4","Bob","electronics",150),
 ("T5","Alice","electronics",200)
]

cust_prod_sales = {}
index = 0
for txn_id,customer,product_type,amount in sales:
    if customer not in cust_prod_sales:
        cust_prod_sales[customer] = {}

    # if product_type not in cust_prod_sales[customer]:
    #     cust_prod_sales[customer][product_type] = amount
    # else:
    #     cust_prod_sales[customer][product_type] += amount
    cust_prod_sales[customer][product_type] = cust_prod_sales[customer].get(product_type,0)+amount




print(cust_prod_sales)