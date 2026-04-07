import numpy as np
import pandas as pd

def process_orders(df):
    df["clean_discount_pct"] = np.where(np.isnan(df["discount_pct"]),0,df["discount_pct"])

    amount_missing = np.isnan(df["amount"])
    invalid_amount = df["amount"] <=0
    invalid_qty = df["qty"] <=0

    df["error_reason"] = np.where(amount_missing,"amount missing","")
    df["error_reason"] = np.where(invalid_amount,"invalid_amount", df["error_reason"])
    df["error_reason"] = np.where(invalid_qty,"invalid_qty",df["error_reason"])

    invalid_mask = amount_missing | invalid_amount | invalid_qty

    df["valid_orders"] = np.where(invalid_mask,"N","Y")
    print(df)

    df["net_amount"] = np.where(invalid_mask,0, df["amount"] - (df["amount"]*df["clean_discount_pct"]/100))

    print(df)

    valid_df = df[df["valid_orders"] == "Y"]
    error_df = df[df["valid_orders"] == "N"]
    return valid_df, error_df

input_df = pd.DataFrame({
        "order_id": [1,2,3,4,5,6],
        "amount": [100, -50, 200, 300, np.nan, 150],
        "qty": [1, 2, 0, 3, 1, -1],
        "discount_pct": [10, 5, np.nan, 20, 15, 10]
    })
valid, error = process_orders(input_df)
