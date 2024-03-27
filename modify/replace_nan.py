import pandas as pd

path = r"C:\Users\pengcheng.yan\Desktop\test_aps\DLL_D50_spec items_240314(1).xlsx"

df = pd.read_excel(path)

# 将所有列中的NaN值替换成"-"
df = df.fillna("-")

df.to_excel(r"C:\Users\pengcheng.yan\Desktop\test_aps\DLL_D50_spec items_240314.xlsx", index=False)