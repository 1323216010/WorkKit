import pandas as pd
import os
from utils import transpose, shaku_list


folder_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\OQC_LH2D'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and 'shakuOQC_BSEC_B_' in filename:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        df_transposed = transpose(df)

        df_transposed = df_transposed[shaku_list()]
        df_transposed['type'] = 'OQC_Largan'

        all_df = pd.concat([all_df, df_transposed], ignore_index=True)



all_df = all_df.sort_values(by='barcode')
all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\aps shaku\Summary Log\OQC_Largan\OQC_Largan shakuOQC_BSEC_B.csv', index=False)