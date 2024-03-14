import pandas as pd
import os
from utils import column, read_csv1

folder_path = r'C:\Users\pengcheng.yan\Desktop\peak search\C3051 search'

# 初始化一个空的 DataFrame 用于存储结果
all_rows = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and 'FineSearch' in filename:
        file_path = os.path.join(folder_path, filename)
        df = read_csv1(file_path, column())

        # 检查 DataFrame 是否为空
        if not df.empty:
            # 假设每个文件的 'barcode' 和 'time' 在所有行中都是相同的
            barcode = df['barcode'].iloc[0]
            time = df['time'].iloc[0]
            row_count = len(df)

            # 创建一个新的 DataFrame 行
            new_row = pd.DataFrame({'filename': [filename], 'barcode': [barcode], 'time': [time], 'row_count': [row_count]})
            all_rows.append(new_row)

# 使用 pd.concat 将所有的行合并成一个 DataFrame
summary_df = pd.concat(all_rows, ignore_index=True)

# 保存汇总结果到 CSV 文件
summary_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\peak search\C3051 search FineSearch.csv', index=False)

