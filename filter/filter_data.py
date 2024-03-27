import os
import pandas as pd
from utils import read_csv


def retain(folder_paths, issue_df):
    matching_data = pd.DataFrame()

    for folder_path in folder_paths:
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)

            df = read_csv(full_path)

            # 通过在df中查找issue_df中存在的barcode来过滤df
            df_filtered = df[df['barcode'].isin(issue_df['barcode'])]

            # 将过滤后的df添加到matching_data
            matching_data = pd.concat([matching_data, df_filtered], ignore_index=True)

    return matching_data


def delete(folder_path, issue_df):
    non_matching_data = pd.DataFrame()

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        df = read_csv(full_path)

        # 使用外连接合并DataFrame，并添加一个指示符列，同时指定唯一的后缀以避免列名冲突
        merged_df = pd.merge(df, issue_df, on=['barcode', 'time'], how='outer', indicator=True, suffixes=('_df', '_issue'))

        # 选择仅在df中存在的行
        non_matched_df = merged_df[merged_df['_merge'] == 'left_only'].drop(columns=['_merge'])

        # 将不匹配的行添加到non_matching_data
        non_matching_data = pd.concat([non_matching_data, non_matched_df], ignore_index=True)

    return non_matching_data



if __name__ == '__main__':
    issue_df = read_csv(r'C:\Users\pengcheng.yan\Desktop\barcode_list.csv')

    folder_paths = [
        r'C:\Users\pengcheng.yan\Desktop\summary log\Module OQC'
    ]
    matching_df = retain(folder_paths, issue_df)
    matching_df.fillna('', inplace=True)  # 用空字符串填充NaN
    matching_df.to_csv(r'C:\Users\pengcheng.yan\Desktop\summary log\summary log.csv', index=False)

