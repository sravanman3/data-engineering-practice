import pandas as pd

data = [
    {"customer": "A", "product_type": "Laptop", "amount": 1000},
    {"customer": "B", "product_type": "Mobile", "amount": 500},
    {"customer": "A", "product_type": "Mobile", "amount": 700},
    {"customer": "A", "product_type": "Laptop", "amount": 300},
    {"customer": "B", "product_type": "Laptop", "amount": 1200},
    {"customer": "B", "product_type": "Nothing", "amount": -10},
    {"customer": "C", "product_type": "Laptop", "amount": "INVALID"}
]
df = pd.DataFrame(data)

df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
error_df = df[df["amount"].isna() | (df["amount"] <=0 )]
df= df[df["amount"].notna()]
df= df[df["amount"] > 0]


customer_summary = (df.groupby("customer",as_index=False)["amount"]
                    .agg(total_rev="sum", total_orders="count",aov="mean"))

top_2 = customer_summary.sort_values("total_rev",ascending=False).head(2)

mixed_metrics = (df.groupby(["customer","product_type"], as_index=False)["amount"]
                 .agg(total_revenue="sum",total_orders="count",avg_order_value="mean"))
print(customer_summary)
print(top_2)
print(mixed_metrics)
print(error_df)