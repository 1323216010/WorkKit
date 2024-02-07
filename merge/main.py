import pandas as pd
import os


folder_path = r'D:\data\VR_output_day_count3'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # 合并DataFrame
        all_df = pd.concat([all_df, df], ignore_index=True)


all_df['day'] = pd.to_datetime(all_df['day'])
# 按day列排序
all_df = all_df.sort_values(by='day')
all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\VR_day_machine_count_summary.csv', index=False)