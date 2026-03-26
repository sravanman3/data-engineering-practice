import pandas as pd

df = pd.read_csv("sales_file.csv")

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
valid_df = df[df["amount"] > 0]
error_df = df[(df["amount"] <= 0) | df["amount"].isna()]
valid_df["tax"] = valid_df["amount"] * 0.1
valid_df["handling_fee"] = valid_df["product_type"].apply(
    lambda x: 20 if x == "Electronics" else 5
)
valid_df["total_amount"] = valid_df["amount"] + valid_df["tax"] + valid_df["handling_fee"]

total_txns = len(df)
error_txns = len(error_df)
failure_rate = round(error_txns / total_txns,2)
print(f"failure_rate: {failure_rate}")

valid_df.to_csv("valid_txns.csv", index=False)
error_df.to_csv("error_txns.csv", index=False)