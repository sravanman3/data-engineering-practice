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

total_amnt_per_cust = {}

for txn_id,customer,product_type,amount in sales:
    total_amnt_per_cust[customer] = total_amnt_per_cust.get(customer,0) + amount

top_customers = sorted(total_amnt_per_cust.items(), key= lambda x:x[1], reverse=True)[:2]

print(top_customers)

rev_per_prd_type = {}

for txn_id,customer,product_type,amount in sales:
    rev_per_prd_type[product_type] = rev_per_prd_type.get(product_type,0) + amount

print(rev_per_prd_type)

txns_per_product = {}

for txn_id,customer,product_type,amount in sales:
    txns_per_product[product_type] = txns_per_product.get(product_type,0) + 1
print(txns_per_product)


customer_summary = {}

for txn_id,customer,product_type,amount in sales:
    if customer not in customer_summary:
        customer_summary[customer] = {"txns":0, "revenue":0}

    customer_summary[customer]["txns"] += 1
    customer_summary[customer]["revenue"] += amount
print(customer_summary)


from collections import defaultdict

customer_summ = defaultdict(lambda: {"txns":0, "revenue":0})

for txn_id,customer,product_type,amount in sales:
    customer_summ[customer]["txns"] += 1
    customer_summ[customer]["revenue"] += amount

print(dict(customer_summ))

product_category = {}
for txn_id,customer,product_type,amount in sales:
    if product_type not in product_category:
        product_category[product_type] = [customer]
    else:
        if customer not in product_category[product_type]:
            product_category[product_type].append(customer)
print(product_category)

prod_category = {}
for txn_id,customer,product_type,amount in sales:
    if product_type not in prod_category:
        prod_category[product_type] = set()
    prod_category[product_type].add(customer)
print(prod_category)