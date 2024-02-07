import pandas as pd
import os

folder_path = 'D:\data\VR_output_day'
output_folder = r'D:\data\VR_output_day_count1'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # 确保day列是日期格式
        df['day'] = pd.to_datetime(df['day'])

        # 分组并计算每个产品对每个ITEM的测试次数
        test_counts = df.groupby(['day', 'BARCODE', 'ITEM']).size().reset_index(name='counts')
        output_path1 = os.path.join(output_folder, '1_' + filename)

        # 先分组，然后对每个组的station列应用一个聚合函数，这里将station列转换为一个由唯一值构成的列表
        test_counts1 = df.groupby(['day', 'BARCODE', 'ITEM']).agg(
            counts=pd.NamedAgg(column='day', aggfunc='size'),  # 计算测试次数
            stations=pd.NamedAgg(column='STATION', aggfunc=lambda x: list(x.unique()))  # 将station列的唯一值转换为列表
        ).reset_index()


        test_counts1.to_csv(output_path1, index=False)

