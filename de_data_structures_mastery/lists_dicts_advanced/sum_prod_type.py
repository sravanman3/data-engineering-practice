sales = [
 ("T1","Alice","electronics",100),
 ("T2","Bob","grocery",200),
 ("T3","Alice","grocery",50),
 ("T4","Bob","electronics",150),
 ("T5","Alice","electronics",200)
]

prod_type_total = {}

for txn_id,customer,product_type,amount in sales:
    prod_type_total[product_type] = prod_type_total.get(product_type,0) + amount

print(prod_type_total)
