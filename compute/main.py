import pandas as pd
from pathlib import Path

def count_csv_rows(directory, output_file):
    total_rows = 0

    csv_files = Path(directory).glob('*.csv')

    barcodes = []  # 用于收集所有文件中的 BARCODE 值


    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        rows = len(df)
        # rows = rows - 1
        total_rows += rows

        print(f"{csv_file.name} has {rows} rows.")

        # 将当前文件的 BARCODE 值添加到列表中
        barcodes.extend(df['barcode'].tolist())

    # 使用集合去除重复的 BARCODE 值，然后计算唯一值的数量
    unique_barcodes_count = len(set(barcodes))

    # 将唯一的 BARCODE 值保存到 CSV 文件
    unique_barcodes_df = pd.DataFrame(set(barcodes), columns=['BARCODE'])
    unique_barcodes_df.to_csv(output_file, index=False)


    print(f"Total rows in all CSV files: {total_rows}")
    print(f"Total unique barcodes across all CSV files: {unique_barcodes_count}")  # 打印所有文件中唯一 barcode 的总数
    print(f"Unique barcodes have been saved to {output_file}")


directory = r'C:\Users\pengcheng.yan\Desktop\tagging_8pixel\input data1'
output_file = r'C:\Users\pengcheng.yan\Desktop\unique_barcodes.csv'
count_csv_rows(directory, output_file)
