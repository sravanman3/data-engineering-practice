from datetime import datetime

class InvalidTransaction(Exception):
    pass


def validate_sales(sales_streaming):


    for txn_id,customer,product,amount in sales_streaming:

        try:
            float_amount = float(amount)
            if float_amount < 0:
                raise InvalidTransaction("NegativeAmount")
            yield "valid",(txn_id,customer,product,float_amount)
            # valid_txns.append((txn_id,customer,product,float_amount))

        except ValueError as e:
            yield "error",{
                "txn_id": txn_id,
                "customer": customer,
                "error_type": "InvalidAmount",
                "error_msg": str(e),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # error_txns.append(
            #     {
            #         "txn_id": txn_id,
            #         "customer": customer,
            #         "error_type": "InvalidAmount",
            #         "error_msg": str(e),
            #         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #     }
            # )
        except InvalidTransaction as e:
            yield "error", {
                "txn_id": txn_id,
                "customer": customer,
                "error_type": "NegativeAmount",
                "error_msg": str(e),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }