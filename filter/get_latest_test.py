import pandas as pd
from utils import read_csv1, summary_bank


sheet1 = pd.read_excel('list.xlsx', sheet_name=0)
list_title = sheet1['title'].tolist() + summary_bank()

path = r'C:\Users\pengcheng.yan\Desktop\1_C2_DPC_Simulation\C2002\ATUN_Dark-D.csv'
df = read_csv1(path, list_title)

df = df[df['barcode'] != '-']
df = df[df['barcode'] != 'barcode']

# 将time列转换为datetime类型
df['time'] = pd.to_datetime(df['time'], format='%Y_%m_%d_%H:%M:%S')

# 删除 'barcode' 和 'time' 列同时相等的重复行，只保留第一次出现的行
df_unique = df.drop_duplicates(subset=['barcode', 'time'])

# 找到每个'barcode'的最新'time'
latest_times = df_unique.groupby('barcode')['time'].max().reset_index()

# 将包含最新时间的DataFrame与原始DataFrame合并，以保留每个'barcode'的最新记录
df_latest = pd.merge(df_unique, latest_times, on=['barcode', 'time'])

# df_latest['time'] = df_latest['time'].str.replace('/', '_').str.replace(' ', '_').str.replace('-', '_')

df_latest.to_csv(r'C:\Users\pengcheng.yan\Desktop\1_C2_DPC_Simulation\C2002.csv', index=False)