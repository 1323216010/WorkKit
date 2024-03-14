
def transpose(df):
    # 转置DataFrame
    df_transposed = df.T

    # 将第一行设置为列标题
    df_transposed.columns = df_transposed.iloc[0]

    # 删除原来的第一行
    df_transposed = df_transposed.drop(df_transposed.index[0])

    # # 删除含有NaN值的列
    # df_transposed = df_transposed.dropna(axis=1, how='any')

    return df_transposed