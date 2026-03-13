sales = [
 ("T1","Alice","electronics",100),
 ("T2","Bob","grocery",200),
 ("T3","Alice","grocery",50),
 ("T4","Bob","electronics",150),
 ("T5","Alice","electronics",200)
]

txns_per_cust = {}
total_amnt_per_cust = {}
for txn_id,customer,product_type,amount in sales:
    txns_per_cust[customer] = txns_per_cust.get(customer,0) + 1
    total_amnt_per_cust[customer] = total_amnt_per_cust.get(customer,0) + amount

print(txns_per_cust)
print(total_amnt_per_cust)
avg = {}
for customer,count in txns_per_cust.items():
    avg[customer] = round(total_amnt_per_cust[customer]/count,2)
    # avg[customer] = round(total_amnt_per_cust[customer] / txns_per_cust[customer],2)

print(avg)
