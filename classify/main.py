import os
import pandas as pd


def extract_datetime(realpath):
    # 假设时间总是位于倒数第二个下划线后
    try:
        datetime_str = realpath.split('_')[-2] + '_' + realpath.split('_')[-1].split('.')[0]
        return pd.to_datetime(datetime_str, format='%Y%m%d_%H%M%S')
    except ValueError:
        return pd.NaT  # 如果转换失败，返回NaT


directory = r'D:\data\VR_output'
for filename in os.listdir(directory):
    source_path = os.path.join(directory, filename)
    df = pd.read_csv(source_path)
    df['time'] = df['FILENAME'].apply(extract_datetime)
    sorted_df = df.groupby('BARCODE').apply(lambda x: x.sort_values('ITEM')).reset_index(drop=True)
    sorted_df.to_csv(source_path, index=False)