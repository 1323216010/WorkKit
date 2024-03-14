import pandas as pd
import os
from utils import transpose


folder_path = r'C:\Users\pengcheng.yan\Desktop\test_aps\doe_log1'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and 'TopLinear' in filename:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        df_transposed = transpose(df)

        all_df = pd.concat([all_df, df_transposed], ignore_index=True)



all_df = all_df.sort_values(by='barcode')
all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\log\C3055\C3055 DOE TopLinear.csv', index=False)