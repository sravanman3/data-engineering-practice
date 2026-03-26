import pandas as pd

sales = pd.read_csv("sales.csv")
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")

customer_sales = sales.merge(customers, on="customer_id", how="inner")

cust_prod_sales = customer_sales.merge(products,on="product_id",how="left")

cust_prod= customer_sales.merge(products,on="product_id",how="left",indicator=True)

print(cust_prod[["product_id","product_name","_merge"]])

cust_prod_sales["error_reason"] = None
cust_prod_sales.loc[cust_prod_sales["category"].isna(),"error_reason"] = "product_id_not_found"

valid_sales = cust_prod_sales[cust_prod_sales["error_reason"].isna()]
invalid_sales = cust_prod_sales[cust_prod_sales["error_reason"].notna()]

segment_summary = (valid_sales.groupby("segment",as_index=False)["amount"]
                   .agg(total_revenue="sum",total_orders="count",average_order_value="mean"))

category_summary = (valid_sales.groupby("category",as_index=False)["amount"]
                    .agg(total_revenue="sum",total_orders="count",average_order_value="mean"))

valid_sales.to_csv("valid_sales.csv",index=False)
invalid_sales.to_csv("invalid_sales.csv",index=False)
segment_summary.to_csv("segment_summary.csv",index=False)
category_summary.to_csv("category_summary.csv",index=False)