import pandas as pd


path = r'C:\Users\pengcheng.yan\Desktop\APS Online\PDX_MFG_Tester_B_Log_20240320215029.csv'

trend_name = pd.read_excel('aps_trend_name.xlsx')
trend_name_cpp = trend_name['C++'].tolist()


df = pd.read_csv(path, usecols=trend_name_cpp, low_memory=False, encoding="UTF-8", delimiter=',')
df = df[trend_name_cpp]

df.to_csv(r'cpp_data.csv', index=False)