import pandas as pd
import glob
import os


folder_path = 'D:/data/VR/*.csv'
output_folder = 'D:/data/VR_output/'

# 确保输出文件夹存在
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

# 计算总文件数
total_files = len(sorted_df) // rows_per_file + 1

# 分割DataFrame并保存为多个CSV文件
for i in range(total_files):
    start_index = i * rows_per_file
    end_index = (i + 1) * rows_per_file
    output_df = sorted_df.iloc[start_index:end_index]
    output_file = os.path.join(output_folder, f'sorted_data_{i+1}.csv')
    output_df.to_csv(output_file, index=False)

    print(f'File {output_file} has been saved.')
