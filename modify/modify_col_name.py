import pandas as pd




csv_file_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\Summary Log\OQC_Largan.csv'


df = pd.read_csv(csv_file_path)


df.columns = [col.replace('OQC_BSEC', '') for col in df.columns]

df.to_csv(csv_file_path, index=False)
