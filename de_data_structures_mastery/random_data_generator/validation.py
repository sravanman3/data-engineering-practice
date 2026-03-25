from datetime import datetime

class InvalidTransaction(Exception):
    pass

def validate_txns(sales):

    error_txns = []
    valid_txns = []


    for txn_id,customer,product,amount in sales:
        try:
            amount_float = float(amount)
            if amount_float < 0:
                raise InvalidTransaction("Amount cannot be negative")

            valid_txns.append((txn_id,customer,product,amount_float))

        except ValueError as e:
            error_txns.append(
                {
                    "txn_id": txn_id,
                    "customer": customer,
                    "error_type": "InvalidAmount",
                    "error_msg": str(e),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        except InvalidTransaction as e:
            error_txns.append(
                {
                    "txn_id": txn_id,
                    "customer": customer,
                    "error_type": "NegativeAmount",
                    "error_msg": str(e),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )

    return valid_txns,error_txns
