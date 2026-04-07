import pandas as pd
import numpy as np

df = pd.DataFrame({
    "amount": [100, -20, 300],
    "qty": [1, 0, 2]
})

valid_mask = (df["amount"] > 0) & (df["qty"] > 0)
df["valid_flag"] = np.where(valid_mask, "Y", "N")
df["final_amount"] = np.where(valid_mask, df["amount"] * df["qty"], 0)
print(df)
