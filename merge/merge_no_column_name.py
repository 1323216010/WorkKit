import pandas as pd


def merge_csvs(csv_with_col_names, csv_without_col_names, output_file):
    # 读取第一个CSV文件，其中包含列名
    df1 = pd.read_csv(csv_with_col_names)

    # 读取第二个CSV文件，没有列名，需要手动指定
    df2 = pd.read_csv(csv_without_col_names, header=None, usecols=[0, 28])
    df2.columns = ['barcode', 'PeakSearch_LowTemp']

    # 去除df2中重复的barcode行，只保留第一次出现的行
    df2 = df2.drop_duplicates(subset=['barcode'], keep='first')

    # 使用barcode列合并两个DataFrame
    merged_df = pd.merge(df1, df2, on='barcode', how='left')

    # 保存合并后的DataFrame到原文件
    merged_df.to_csv(output_file, index=False)


csv_with_col_names = r'C:\Users\pengcheng.yan\Desktop\peak search\C3051 search FineSearch.csv'  # 第一个CSV文件的路径
csv_without_col_names = r'C:\Users\pengcheng.yan\Desktop\peak search\C3051.csv'  # 第二个CSV文件的路径

merge_csvs(csv_with_col_names, csv_without_col_names, csv_with_col_names)
