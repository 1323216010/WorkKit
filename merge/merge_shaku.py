import pandas as pd
import os
from functools import reduce


folder_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\Summary Log\OQC_MTM'

dataframes = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        dataframes.append(df)

merged_df = dataframes[0]
for df in dataframes[1:]:
    merged_df = pd.merge(merged_df, df, on=['barcode', 'type'], how='inner')

merged_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\aps shaku\Summary Log\OQC_MTM.csv', index=False)