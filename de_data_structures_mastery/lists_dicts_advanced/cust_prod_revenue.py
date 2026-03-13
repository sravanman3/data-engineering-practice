from collections import defaultdict


sales = [
 ("T1","Alice","electronics",120),
 ("T2","Bob","grocery",80),
 ("T3","Charlie","electronics",200),
 ("T4","Alice","grocery",60),
 ("T5","Bob","electronics",150),
 ("T6","David","grocery",40),
 ("T7","Charlie","grocery",90),
 ("T8","Eve","electronics",70),
 ("T9","Alice","electronics",110),
 ("T10","David","electronics",30)
]
# cust_prod_rev = defaultdict(dict)
# for txn_id,customer,product_type,amount in sales:
#     cust_prod_rev[customer][product_type] = cust_prod_rev[customer].get(product_type,0) + amount
# print(dict(cust_prod_rev))


cust_prod_revenue = defaultdict(lambda: defaultdict(int))
for txn_id,customer,product_type,amount in sales:
    cust_prod_revenue[customer][product_type] += amount

result = {cust: dict(prod) for cust,prod in cust_prod_revenue.items()}
print(result)


rev_per_cust = defaultdict(int)
for txn_id,customer,product_type,amount in sales:
    rev_per_cust[customer] += amount
result = sorted(rev_per_cust.items(), key=lambda x:x[1], reverse=True)[:3]
print(result)