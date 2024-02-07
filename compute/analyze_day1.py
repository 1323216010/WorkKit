import pandas as pd
import os


folder_path = r'D:\data\PDX_output_day_count'
output_folder = r'D:\data\PDX_output_day_count_analysis'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def count_barcode_ranges(group):
    return pd.Series({
        'counts_sum': group['counts'].sum(),
        'total_count': group['BARCODE'].nunique(),
        'less_than_5': group[group['counts'] < 5]['BARCODE'].nunique(),
        'between_5_and_9': group[(group['counts'] >= 5) & (group['counts'] < 10)]['BARCODE'].nunique(),
        'between_10_and_19': group[(group['counts'] >= 10) & (group['counts'] < 20)]['BARCODE'].nunique(),
        'between_20_and_50': group[(group['counts'] >= 20) & (group['counts'] <= 50)]['BARCODE'].nunique(),
        'between_51_and_100': group[(group['counts'] > 50) & (group['counts'] <= 100)]['BARCODE'].nunique(),
        'between_101_and_500': group[(group['counts'] > 100) & (group['counts'] <= 500)]['BARCODE'].nunique(),
        'greater_than_500': group[group['counts'] > 500]['BARCODE'].nunique()
    })

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # 创建映射表存储每个(day, Truncated_ITEM)对应的STATION
        station_mapping = df.groupby(['day', 'ITEM'])['stations'].apply(set).reset_index()
        station_mapping['stations'] = station_mapping['stations'].apply(lambda x: ', '.join(x))  # 将STATION集合转换为字符串

        # 对每一天的每个Truncated_ITEM分组，计算符合条件的BARCODE数量以及总数
        results = df.groupby(['day', 'ITEM']).apply(count_barcode_ranges).reset_index()

        # 将STATION信息合并到结果中
        results = results.merge(station_mapping, on=['day', 'ITEM'], how='left')

        output_path = os.path.join(output_folder, '1_' + filename)
        results.to_csv(output_path, index=False)
