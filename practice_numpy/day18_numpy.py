import numpy as np

ages = np.array([25,-18,2,0,-29,36])

valid_ages = np.where(ages <= 0, 18, ages)
print(valid_ages)

salary = np.array([50000.0, np.nan, 65000.0, np.nan, 72000.0])
masked_sal = np.isnan(salary)
valid_sal = np.where(masked_sal, 0 , salary)
print(valid_sal)
print(masked_sal)
print(len(salary[masked_sal]))
print(masked_sal.sum())

txn_id = np.array([1,2,3,4,5])
amount  = np.array([100.0, -20.0, np.nan, 250.0, 300.0])
qty     = np.array([1, 2, 3, 0, 5])

masked_amount = np.isnan(amount)
invalid_amount = amount <= 0
invalid_qty = qty <= 0
invalid_txn_ids = masked_amount | invalid_amount | invalid_qty
valid_txn_ids = ~invalid_txn_ids
print(txn_id[invalid_txn_ids])
print(txn_id[valid_txn_ids])


product_price = np.array([100.0, -50.0, np.nan, 200.0, 150.0])
discount_pct  = np.array([10.0, 5.0, 20.0, np.nan, -10.0])

masked_price = np.isnan(product_price)
invalid_price = product_price <= 0

invalid_prod_price = masked_price | invalid_price
print(invalid_prod_price)
valid_prod_price = ~invalid_prod_price
print(product_price[valid_prod_price])

valid_disc_pct = np.where(discount_pct <0, 0 , discount_pct)
final_disc_pct = np.where(np.isnan(valid_disc_pct), 0 , valid_disc_pct)
print(final_disc_pct)

discounted_price = product_price[valid_prod_price] - ((product_price[valid_prod_price] * final_disc_pct[valid_prod_price])/100)
print(discounted_price)

