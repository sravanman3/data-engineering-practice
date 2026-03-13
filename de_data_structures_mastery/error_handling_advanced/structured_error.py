from datetime import datetime

class InvalidTransaction(Exception):
    pass
valid_txns = []
error_logs = []

sales = [
 ("T1","Alice","electronics",120),
 ("T2","Bob","grocery","INVALID"),
 ("T3","Charlie","electronics",-200),
 ("T4","Alice","grocery",60),
 ("T5","David","electronics","50"),
 ("T6","Eve","grocery",-10)
]

for txn_id,customer,product_type,amount in sales:
    try:
        amount_float = float(amount)

        if amount_float < 0:
            raise InvalidTransaction("Amount cannot be negative")
        valid_txns.append((txn_id,customer,product_type,amount_float))

    except ValueError as e:
        error_logs.append({
            "txn_id": txn_id,
            "customer": customer,
            "error_type": "InvalidAmountFormat",
            "error_msg": str(e),
            "update_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    except InvalidTransaction as e:
        error_logs.append({
            "txn_id": txn_id,
            "customer": customer,
            "error_type": "NegativeAmount",
            "error_msg": str(e),
            "update_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

print(valid_txns)
print(error_logs)