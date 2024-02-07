import pandas as pd
import os
import dask.dataframe as dd

def extract_datetime(realpath):
    try:
        datetime_str = realpath.split('_')[-2] + '_' + realpath.split('_')[-1].split('.')[0]
        return pd.to_datetime(datetime_str, format='%Y%m%d_%H%M%S')
    except ValueError:
        return pd.NaT

folder_path = 'D:/data/PDX/*.csv'
output_folder = 'D:/data/PDX_output_day/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

ddf = dd.read_csv(folder_path, dtype={'MACHINENAME': 'object'})

# 对FILENAME应用日期提取函数
ddf['time'] = ddf.map_partitions(lambda df: df.apply(lambda row: extract_datetime(row['FILENAME']) if 'FILENAME' in df.columns else pd.NaT, axis=1), meta='datetime64[ns]')

# 将time列转换为日期类型并添加day列
ddf['day'] = ddf['time'].dt.date

# 按day分组并进行排序
sorted_ddf = ddf.groupby(['day', 'BARCODE']).apply(lambda x: x, meta=ddf).reset_index(drop=True)

# 计算完成后，将Dask DataFrame转换为Pandas DataFrame
sorted_df = sorted_ddf.compute()

# 初始化文件编号和当前文件的行计数器
rows_per_file = 1000000
file_number = 0
current_file_rows = 0


for day, group in sorted_df.groupby('day'):
    # 如果当前文件加上这个组的行数将超过限制，则开始新文件
    if current_file_rows + len(group) > rows_per_file:
        file_number += 1
        current_file_rows = 0  # 重置行计数器

    output_file = os.path.join(output_folder, f'sorted_data_{file_number}.csv')

    # 如果是新文件或文件不存在，则直接写入，否则追加
    if current_file_rows == 0 or not os.path.exists(output_file):
        group.to_csv(output_file, index=False)
    else:
        group.to_csv(output_file, mode='a', index=False, header=False)

    # 更新当前文件的行计数器
    current_file_rows += len(group)

    print(f'Day {day} has been added to {output_file}')
