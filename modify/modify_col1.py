import pandas as pd
import os


folder_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\Summary Log\OQC_MTM\新建文件夹'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    df = pd.read_csv(file_path)

    # 指定不需要修改的列名
    excluded_columns = ['barcode', 'type']

    suffix = filename.replace('.csv', '')
    suffix = suffix.replace('OQC_MTM ', '')
    suffix = '_' + suffix

    # 修改除了excluded_columns之外的所有列名
    df.columns = [f'{col}{suffix}' if col not in excluded_columns else col for col in df.columns]

    df.to_csv(file_path, index=False)
