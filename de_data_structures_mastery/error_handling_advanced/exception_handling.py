sales = [
 ("T1","Alice","electronics",120),
 ("T2","Bob","grocery","INVALID"),
 ("T3","Charlie","electronics",-200),
 ("T4","Alice","grocery",60)
]

valid_txns = []
error_txns = []

for txn_id,customer,product_type,amount in sales:
    try:
        float_amount = float(amount)
        if float_amount < 0:
            raise ValueError("Negative amount")

        valid_txns.append((txn_id,customer,product_type,float_amount))
    except ValueError as e:
        error_txns.append(f"Error for txn_id: {txn_id} : {str(e)}")

print(error_txns)
print(valid_txns)