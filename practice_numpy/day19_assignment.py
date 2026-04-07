import pandas as pd
import numpy as np

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "amount": [100, 200, -50, 300, 0],
    "discount_pct": [10, 20, 5, np.nan, 15],
    "qty": [1, 2, 1, 3, 0]
})

df["clean_discount_pct"] = np.where(np.isnan(df["discount_pct"]), 0 , df["discount_pct"] )

valid_mask = (df["amount"] >0) & (df["qty"] >0)
df["valid_order"] = np.where(valid_mask, "Y","N")

df["net_amount"] = np.where(valid_mask,
                            df["amount"] - (df["amount"] * df["clean_discount_pct"]/100),
                            0)

invalid_amount = df["amount"] <=0
invalid_qty = df["qty"] <= 0

df["error_reason"] = np.where(invalid_amount,"invalid amount" , "")
df["error_reason"] = np.where(invalid_qty,"invalid qty" , df["error_reason"])

print(df)