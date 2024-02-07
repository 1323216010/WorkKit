import pandas as pd
import glob
import os


folder_path = 'D:/data/VR/*.csv'
output_folder = 'D:/data/VR_output/'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


csv_files = glob.glob(folder_path)

# 读取所有csv文件并合并为一个DataFrame
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# 按barcode分组，然后在每个组内按index排序
sorted_df = combined_df.groupby('BARCODE').apply(lambda x: x.sort_values('BARCODE_INDEX')).reset_index(drop=True)

# 确定每个文件的行数，例如每个文件大约100万行
rows_per_file = 1000000

# 初始化文件编号和当前文件的行计数器
file_number = 0
current_file_rows = 0

# 遍历每个分组
for barcode, group in sorted_df.groupby('BARCODE'):
    # 如果当前文件加上这个组的行数将超出限制，则开始新文件
    if current_file_rows + len(group) > rows_per_file:
        file_number += 1
        current_file_rows = 0  # 重置行计数器

    # 计算输出文件路径
    output_file = os.path.join(output_folder, f'sorted_data_{file_number+1}.csv')

    # 如果是新文件或文件不存在，则直接写入，否则追加
    if current_file_rows == 0 or not os.path.exists(output_file):
        group.to_csv(output_file, index=False)
    else:
        group.to_csv(output_file, mode='a', index=False, header=False)

    # 更新当前文件的行计数器
    current_file_rows += len(group)

    print(f'Barcode {barcode} has been added to {output_file}')
