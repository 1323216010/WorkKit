from utils import read_csv


path = r'C:\Users\pengcheng.yan\Desktop\summary log.csv'
df = read_csv(path)

issue_df = read_csv(r'C:\Users\pengcheng.yan\Desktop\barcode_list.csv')

# # 删除 'barcode' 和 'vcmID' 列同时相等的重复行，只保留第一次出现的行
# df = df.drop_duplicates(subset=['barcode', 'vcmID'])

df_filtered = df[df['barcode'].isin(issue_df['barcode'])]

df_filtered.to_csv(path, index=False)

print(df_filtered)
