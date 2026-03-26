import pandas as pd

fee = {"Electronics": 20, "Clothing": 10}

df = pd.read_csv("sales_file.csv")

df["amount"] = pd.to_numeric(df["amount"], errors = "coerce")

valid_df = df[df["amount"] > 0]
error_df = df[df["amount"].isna() | (df["amount"] <= 0)]

valid_df["tax"] = valid_df["amount"] * 0.1
valid_df["handling_fee"] = valid_df["product_type"].apply(
    lambda x: 20 if x == "Electronics"
    else 10 if x == "Clothing"
    else 5)

valid_df["fee"] = valid_df["product_type"].map(fee).fillna(5)

valid_df["total_amount"] = valid_df["amount"] + valid_df["tax"] + valid_df["handling_fee"]

total_txns = len(df)
error_txns = len(error_df)

failure_rate = error_txns / total_txns
print(f"failure_rate: {failure_rate}")

valid_df.to_csv("valid_pandas.csv",index=False)
error_df.to_csv("error_pandas.csv",index=False)

customer_summary = valid_df.groupby("customer")["amount"].sum().reset_index()
product_summary  = valid_df.groupby("product_type")["amount"].sum()
# customer_metrics = valid_df.groupby("customer")["amount"].agg(["sum","count","mean","max","min"])
customer_metrics = valid_df.groupby("customer")["amount"].agg(
    total_revenue = "sum",
    total_orders = "count",
    avg_order_value = "mean",
    max_order_value = "max",
    min_order_value = "min"
).reset_index()

top_customers = (valid_df.groupby("customer")["amount"]
                 .sum()
                 .sort_values(ascending = False)
                 .head(3))

print(top_customers)

t_customers = (valid_df.groupby("customer",as_index=False)["amount"]
               .sum()
               .sort_values("amount", ascending=False)
               .head(3))
print(t_customers)
aov = valid_df["amount"].mean()
print(aov)

customer_aov = valid_df.groupby("customer")["amount"].mean().reset_index(name="aov")
print(customer_aov)

multi_summary = (valid_df.groupby(["customer","product_type"])["amount"]
                 .agg(total_rev = "sum",
                      total_orders = "count",
                      avg = "mean")
                 .sort_values(["customer","avg"], ascending=[True,False])
                 .reset_index())
print(multi_summary)

customer_summary.to_csv("customer_summary.csv",index=False)
multi_summary.to_csv("multi_summary.csv",index=False)