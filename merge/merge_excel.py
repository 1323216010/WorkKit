import pandas as pd
import os
from utils import summary_cal, read_csv1, read_csv


folder_path = r'C:\Users\pengcheng.yan\Desktop\test_pit'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        # df = read_csv1(file_path, summary_cal())
        df = pd.read_excel(file_path, engine='openpyxl')

        # 合并DataFrame
        all_df = pd.concat([all_df, df], ignore_index=True)




all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\bank.csv', index=False)