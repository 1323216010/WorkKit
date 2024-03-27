import pandas as pd
import os


def remove_columns(merged_df):
    columns_to_remove = []
    for col in merged_df.columns:
        if col.endswith('_x'):
            original_col_name = col[:-2]  # 去除_x后缀获取原始列名
            col_y = original_col_name + '_y'

            # 如果存在对应的_y列，可以选择删除_y列
            if col_y in merged_df.columns:
                columns_to_remove.append(col_y)

            # 重命名_x列为原始列名
            merged_df.rename(columns={col: original_col_name}, inplace=True)

    # 删除所有标记为删除的列
    merged_df.drop(columns=columns_to_remove, inplace=True)

    return merged_df


ftu_path = r'C:\Users\pengcheng.yan\Desktop\Merged_Testlog\Merged-FTU.csv'
df_ftu = pd.read_csv(ftu_path)
ftu_list = df_ftu.columns

folder_path = r'C:\Users\pengcheng.yan\Desktop\Merged_Testlog\FTU'

list1 = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        common_columns = [col for col in df.columns if col in df_ftu.columns]
        df = df[common_columns]
        list1.append(df)


merged_df = list1[0]
for df in list1[1:]:
    merged_df = pd.merge(merged_df, df, on=['barcode', 'global_time_stamp', 'PASS_FAIL'], how='inner')
    remove_columns(merged_df)
    print()



# merged_df = merged_df.sort_values(by='barcode')
merged_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\Merged_Testlog\FTU.csv', index=False)