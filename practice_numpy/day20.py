import time

import pandas as pd
import numpy as np

np.random.seed(42)

n = 100000

df = pd.DataFrame({
    "amount": np.random.randint(-100, 500, n),
    "qty": np.random.randint(0, 5, n),
    "discount_pct": np.random.choice([5, 10, 15, np.nan], n)
})


def cal_net(row):
    if row["amount"] > 0 and row["qty"] > 0:
        discount = 0 if pd.isna(row["discount_pct"]) else row["discount_pct"]
        return row["amount"] -(row["amount"]*discount/100)
    return 0

start = time.time()
df["net_apply"] = df.apply(cal_net, axis=1)
print("Apply time:", time.time() - start)

start_time = time.time()
clean_discount = np.where(np.isnan(df["discount_pct"]),0,df["discount_pct"])
valid_mask = (df["amount"] >0) & (df["qty"] > 0)
df["net_vectorized"] = np.where(valid_mask,
                                df["amount"] - (df["amount"] * clean_discount/100),
                                0)
print("vectorized time:", time.time() - start_time)
