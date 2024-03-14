import os
import pandas as pd


folder_path = r'C:\Users\pengcheng.yan\Desktop\tagging_8pixel\input data1'
output_path = r'C:\Users\pengcheng.yan\Desktop\tagging_8pixel\input data2'

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # 替换列名中的 '#' 字符
        df.columns = [col.replace('#', '') for col in df.columns]
        df.rename(columns={'barcode': 'BARCODE'}, inplace=True)

        # 过滤掉第二和第三行（索引为1和2的行）
        df = df.drop([0, 1])

        # 过滤掉包含 NaN 的行
        df = df.dropna()

        output_file_path = os.path.join(output_path, f"{os.path.splitext(filename)[0]}.csv")

        df.to_csv(output_file_path, index=False)


