import pandas as pd
import os
from utils import transpose


folder_path = r'C:\Users\pengcheng.yan\Desktop\96 pcs Top Besc\[PDX_Cowell]APS 50pcs LD Soaking Time DOE 20240316\Cube OQC\shaku'

all_df = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and 'BSEC_TopLinear' in filename:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        df_transposed = transpose(df)

        df_transposed = df_transposed[['barcode', 'wide_aps_sensor_bottomEndStop_temp']]
        df_transposed['type'] = 'wide_endstop_apstemp'

        all_df = pd.concat([all_df, df_transposed], ignore_index=True)



all_df = all_df.sort_values(by='barcode')
all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\96 pcs Top Besc\50pcs OQC Top .csv', index=False)