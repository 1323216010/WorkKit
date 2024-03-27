import pandas as pd
import os

folder_path = r'C:\Users\pengcheng.yan\Desktop\test_pit\D50 1pc (OQC)'


dfs = []

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.xlsx'):
            file_path = os.path.join(dirpath, filename)
            df = pd.read_excel(file_path, engine='openpyxl')
            dfs.append(df)

if dfs:
    # 获取所有DataFrame的列的交集
    common_columns = set(dfs[0].columns)
    for df in dfs[1:]:
        common_columns.intersection_update(df.columns)

    # 保持第一个DataFrame的列顺序
    common_columns_ordered = [col for col in dfs[0].columns if col in common_columns]

    # 选择每个DataFrame的共有列并合并，保持列顺序
    all_df = pd.concat([df[common_columns_ordered] for df in dfs], ignore_index=True)

    all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\bank_d50.csv', index=False)
else:
    print("No data frames to process.")
