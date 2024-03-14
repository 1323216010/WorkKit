import pandas as pd


file_path = r'C:\Users\pengcheng.yan\Desktop\test\results.csv'
df = pd.read_csv(file_path)

df['time'] = df['time'].str[:8] + '_' + df['time'].str[8:]
df.to_csv(file_path, index=False)