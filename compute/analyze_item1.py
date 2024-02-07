import pandas as pd
import os, json


with open(r'config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


directory = config['data_path']
output_folder = config['output_path']


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


item_counts = {}
barcode_item_counts = {}


for filename in os.listdir(directory):
    source_path = os.path.join(directory, filename)

    print(source_path)
    df = pd.read_csv(source_path)

    # 更新ITEM的总出现次数
    for item in df['ITEM']:
        item_counts[item] = item_counts.get(item, 0) + 1

    # 对于每个BARCODE下的ITEM计数
    for _, row in df.iterrows():
        barcode = row['BARCODE']
        item = row['ITEM']
        barcode_item_key = (barcode, item)
        barcode_item_counts[barcode_item_key] = barcode_item_counts.get(barcode_item_key, 0) + 1


output_csv_path = os.path.join(output_folder, 'item_counts_summary.csv')


barcode_item_df = pd.DataFrame(list(barcode_item_counts.items()), columns=['Barcode_Item', 'Count'])
barcode_item_df[['BARCODE', 'ITEM']] = pd.DataFrame(barcode_item_df['Barcode_Item'].tolist(), index=barcode_item_df.index)
counts_over_threshold = barcode_item_df.groupby('ITEM')['Count'].agg(
    Counts_Under_20=lambda x: (x < 20).sum(),
    Counts_Over_20=lambda x: (x > 20).sum(),
    Counts_Over_50=lambda x: (x > 50).sum(),
    Counts_Over_100=lambda x: (x > 100).sum()
).reset_index()

# 合并总计数和超过阈值的计数
item_counts_df = pd.DataFrame(list(item_counts.items()), columns=['ITEM', 'Total_Counts'])
summary_df = pd.merge(item_counts_df, counts_over_threshold, on='ITEM', how='left')


summary_df.to_csv(output_csv_path, index=False)