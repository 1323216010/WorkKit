import pandas as pd


doe_path = r'C:\Users\pengcheng.yan\Desktop\log\C3054 DOE TopLinear.csv'
por_path = r'C:\Users\pengcheng.yan\Desktop\log\C3054 POR TopLinear.csv'

df_doe = pd.read_csv(doe_path)
df_doe['Type'] = 'DOE'

df_por = pd.read_csv(por_path)
df_por['Type'] = 'POR'


all_df = pd.concat([df_por, df_doe], ignore_index=True)

# # 将'Type'列移至首位
# all_df = all_df[['Type'] + [col for col in all_df.columns if col != 'Type']]
all_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\log\DOE&POR.csv', index=False)