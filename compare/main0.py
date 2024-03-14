import pandas as pd
from utils_search import read_csv


df1 = read_csv(r'C:\Users\pengcheng.yan\Desktop\PIT FTD\POR.csv')
# df1 = df1.loc[df1['PASS_FAIL'] == 'PASS']

df2 = read_csv(r'C:\Users\pengcheng.yan\Desktop\PIT FTD\Bulk mode.csv')
# df2 = df2.loc[df2['PASS_FAIL'] == 'PASS']


# 合并两个DataFrame，基于'barcode'和'Global_TimeStamp'列
merged_df = pd.merge(df1, df2, on=['barcode'], suffixes=('_POR', '_BulkMode'))

# 同时检查'#Bank0'和'#Bank1'列的值是否相等
# merged_df['#Bank155_equal'] = merged_df['#Bank155_T0'] == merged_df['#Bank155_Retest']
# merged_df['#Bank156_equal'] = merged_df['#Bank156_T0'] == merged_df['#Bank156_Retest']
# merged_df['#Bank157_equal'] = merged_df['#Bank157_T0'] == merged_df['#Bank157_Retest']
# merged_df['#Bank158_equal'] = merged_df['#Bank158_T0'] == merged_df['#Bank158_Retest']
#
# merged_df['both_equal'] = merged_df['#Bank155_equal'] & merged_df['#Bank156_equal'] & merged_df['#Bank157_equal'] & merged_df['#Bank158_equal']

merged_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\PIT FTD\POR and Bulk Mode.csv', index=False)


print()
