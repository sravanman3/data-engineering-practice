from collections import defaultdict
import json
import csv

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

product_summary = defaultdict(set)

for txn_id,customer,product_type,amount in sales:
    product_summary[product_type].add(customer)

print(dict(product_summary))

with open("product_summary.csv","w",newline='') as f:
    csvwriter = csv.DictWriter(f,fieldnames=["Electronics","Grocery"])
    csvwriter.writeheader()
    csvwriter.writerows(dict(product_summary))