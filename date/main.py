import pandas as pd
import glob
import os


def extract_datetime(realpath):
    # 假设时间总是位于倒数第二个下划线后
    try:
        datetime_str = realpath.split('_')[-2] + '_' + realpath.split('_')[-1].split('.')[0]
        return pd.to_datetime(datetime_str, format='%Y%m%d_%H%M%S')
    except ValueError:
        return pd.NaT


folder_path = r'D:\data\PDX\*.csv'
output_folder = r'D:\data\PDX_output_day'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

csv_files = glob.glob(folder_path)

# 读取所有csv文件并合并为一个DataFrame
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# 使用向量化的字符串分割功能来提取时间戳部分
split_filenames = combined_df['FILENAME'].str.rsplit('_', n=2)
datetime_str_series = split_filenames.str[-2] + '_' + split_filenames.str[-1].str.split('.').str[0]

# 将这个Series转换为datetime类型
combined_df['time'] = pd.to_datetime(datetime_str_series, format='%Y%m%d_%H%M%S', errors='coerce')
combined_df['day'] = combined_df['time'].dt.date

# 先按day分组，再在同一天内按BARCODE分组
sorted_df = combined_df.sort_values(by=['day', 'BARCODE'])

# 确定每个文件的行数，例如每个文件大约100万行
rows_per_file = 1000000

# 初始化文件编号和当前文件的行计数器
file_number = 0
current_file_rows = 0

# 遍历每个分组
for barcode, group in sorted_df.groupby('day'):
    # 如果当前文件加上这个组的行数将超出限制，则开始新文件
    if current_file_rows + len(group) > rows_per_file:
        file_number += 1
        current_file_rows = 0  # 重置行计数器

    # 计算输出文件路径
    output_file = os.path.join(output_folder, f'sorted_data_{file_number + 1}.csv')

    # 如果是新文件或文件不存在，则直接写入，否则追加
    if current_file_rows == 0 or not os.path.exists(output_file):
        group.to_csv(output_file, index=False)
    else:
        group.to_csv(output_file, mode='a', index=False, header=False)

    # 更新当前文件的行计数器
    current_file_rows += len(group)

    print(f'Barcode {barcode} has been added to {output_file}')
