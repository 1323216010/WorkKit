from utils import read_csv


path = r'D:\project\Python\WorkBox\draw\APS_VCM_Sweep\SerachLog\df_module.csv'
df = read_csv(path)



# 删除 'barcode' 和 'vcmID' 列同时相等的重复行，只保留第一次出现的行
df_unique = df.drop_duplicates(subset=['barcode', 'vcmID'])

df_unique.to_csv(path, index=False)

print(df_unique)
