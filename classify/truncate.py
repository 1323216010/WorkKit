import pandas as pd
import os, re


# 截断-符号后紧接数字的ITEM
def truncate_item(item):
    # 查找-后直接跟随数字的模式，并截断
    truncated = re.sub(r'-\d.*', '', item)
    return truncated

folder_path = r'D:\data\VR_output_day_count1'
output_folder = r'D:\data\VR_output_day_count2'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        summary_df = pd.read_csv(file_path)

        # 应用该函数到ITEM列
        summary_df['Truncated_ITEM'] = summary_df['ITEM'].apply(truncate_item)

        # 对截断后的ITEM进行分组，合计相关列
        aggregated_df = summary_df.groupby(['day', 'BARCODE', 'Truncated_ITEM']).agg({
            'counts': 'sum'
        }).reset_index()

        output_path = os.path.join(output_folder, '1_' + filename)
        aggregated_df.to_csv(output_path, index=False)






