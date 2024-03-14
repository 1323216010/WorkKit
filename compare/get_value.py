import os
import shutil
import pandas as pd
from datetime import datetime
from utils_search import get_value_from_csv

# 转换时间格式的函数
def convert_time_format(time_str):
    dt = datetime.strptime(time_str, '%Y_%m_%d_%H:%M:%S')
    return dt.strftime('%Y%m%d_%H%M%S')

# 寻找包含barcode和time的文件并移动，同时更新DataFrame
def find_files_with_barcode_and_time(row, directory, df):
    for filename in os.listdir(directory):
        if row['barcode'] in filename:
            source_path = os.path.join(directory, filename)
            df.at[row.name, 'Delta_Map_BulkMode'] = get_value_from_csv(row['#dpc_D50_POS_X_POR'], row['#dpc_D50_POS_Y_POR'], source_path)

# 读取DataFrame
df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\PIT FTD\POR and Bulk Mode.csv')

# 初始化'file'列
df['Delta_Map_BulkMode'] = ''

# 源目录和目标目录路径
directory = r'C:\Users\pengcheng.yan\Desktop\test_pit\BulkMode'

# 遍历DataFrame中的每一行，寻找并移动文件，同时更新DataFrame
for index, row in df.iterrows():
    find_files_with_barcode_and_time(row, directory, df)

df.to_csv(r'C:\Users\pengcheng.yan\Desktop\PIT FTD\POR and Bulk Mode.csv', index=False)
print()
