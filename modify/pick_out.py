import json
import pandas as pd



df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\test_log\500pcs_por.csv')

with open('paths.json', 'r', encoding='utf-8') as file:
    file_paths = json.load(file)

target_paths = []

for index, row in df.iterrows():
    barcode = row['barcode']
    time = row['time']
    time = time.replace('_', '')

    filtered_paths = [
        path for path in file_paths
        if barcode in path and time in path
    ]

    target_paths += filtered_paths


with open('target_paths.json', 'w', encoding='utf-8') as file:
    json.dump(target_paths, file, ensure_ascii=False, indent=4)

