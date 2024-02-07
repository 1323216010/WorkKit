import pandas as pd
import os

folder_path = r'D:\data\VR_output_day'
output_folder = r'D:\data\VR_output_day_count3'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # 确保day列是日期格式
        df['day'] = pd.to_datetime(df['day'])

        # 用 'Unknown' 替换 NaN 值
        df['MACHINENAME'] = df['MACHINENAME'].fillna('Unknown')

        # 分组并计算每个产品对每个ITEM的测试次数
        test_counts = df.groupby(['day', 'MACHINENAME']).size().reset_index(name='counts')
        output_path1 = os.path.join(output_folder, '1_' + filename)

        test_counts.to_csv(output_path1, index=False)
