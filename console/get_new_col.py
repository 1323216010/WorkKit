import os
import pandas as pd


def extract_vcmID(sn):
    parts = sn.split('_')
    if len(parts) > 3:
        return parts[3]  # 返回第三个下划线到第四个下划线之间的子串
    else:
        return ''


def get_new_col(path):
    df = pd.read_csv(path)

    df['vcmID'] = df['SN'].apply(extract_vcmID)
    df = df[['vcmID'] + [col for col in df.columns if col != 'vcmID']]

    df.to_csv(path, index=False)


folder_path = r'C:\Users\pengcheng.yan\Desktop\OQC APS Cal\OQC APS Cal Simulation'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        get_new_col(file_path)
