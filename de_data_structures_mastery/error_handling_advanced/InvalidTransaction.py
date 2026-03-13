class InvalidTransaction(Exception):
    pass

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
        amount_float = float(amount)
        if amount_float < 0:
            raise InvalidTransaction(f"Amount can not be negative")
        valid_txns.append((txn_id,customer,product_type,amount_float))
    except ValueError as e:
        error_txns.append(f"Amount must be numeric for txn_id: {txn_id}")
    except InvalidTransaction as e:
        error_txns.append(f"Error in txn_id: {txn_id} : {e}")
print(valid_txns)
print(error_txns)

