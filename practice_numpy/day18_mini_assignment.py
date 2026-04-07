import numpy as np

order_id = np.array([101, 102, 103, 104, 105, 106, 107])
amount   = np.array([250.0, np.nan, -40.0, 500.0, 100.0, 0.0, 300.0])
qty      = np.array([2, 1, 3, 0, 5, 2, -1])
fee      = np.array([10.0, np.nan, 5.0, 20.0, -2.0, 8.0, 15.0])


missing_amount = np.isnan(amount)
invalid_amount = amount <=0
amount_masked = missing_amount | invalid_amount
invalid_amount = amount[amount_masked]
valid_amount_masked = ~amount_masked
valid_amount = amount[valid_amount_masked]

masked_qty = qty <=0
invalid_qty = qty[masked_qty]
valid_masked_qty = ~masked_qty
valid_qty = qty[valid_masked_qty]
print(invalid_qty)
print(valid_qty)

clean_fee = np.where(np.isnan(fee), 0 , fee)
final_fee = np.where(clean_fee <=0, 0 , clean_fee)

print("cleaned fee: ", final_fee)

masked_order_ids = amount_masked | masked_qty
valid_masked_order_ids = ~masked_order_ids
print("valid order ids: " , order_id[valid_masked_order_ids])
print("invalid order ids: " , order_id[masked_order_ids])

total_amount = amount[valid_masked_order_ids] + final_fee[valid_masked_order_ids]
print("total amount: ", total_amount)