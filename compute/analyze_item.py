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


data_for_csv = []
for item, count in item_counts.items():
    data_for_csv.append({
        'ITEM': item,
        'Total_Counts': count,
        'Counts_Over_20': sum(1 for key, value in barcode_item_counts.items() if value > 20 and key[1] == item),
        'Counts_Over_50': sum(1 for key, value in barcode_item_counts.items() if value > 50 and key[1] == item),
        'Counts_Over_100': sum(1 for key, value in barcode_item_counts.items() if value > 100 and key[1] == item),
    })


summary_df = pd.DataFrame(data_for_csv)


output_csv_path = os.path.join(output_folder, 'item_counts_summary.csv')
summary_df.to_csv(output_csv_path, index=False)
