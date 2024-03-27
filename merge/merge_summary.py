import pandas as pd
import os
from utils import read_csv


folder_path = r'C:\Users\pengcheng.yan\Desktop\summary log\Module OQC'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # df = read_csv1(file_path, summary_cal())
        df = read_csv(file_path)

        # 合并DataFrame
        all_df = pd.concat([all_df, df], ignore_index=True)


all_df = all_df.sort_values(by='barcode')
all_df = all_df.loc[all_df['#PASS_FAIL'] == 'PASS']
# all_df = all_df.drop_duplicates(subset='barcode', keep='first')

all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\por summary log.csv', index=False)