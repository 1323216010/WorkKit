import pandas as pd


def save_range_to_csv(df, row_start, row_end, col_start, col_end, output_path):
    """
    将指定范围的DataFrame数据保存到CSV文件中，并在文件中包含行和列的起始索引信息。
    数据中包含行索引和列索引。

    :param df: DataFrame对象。
    :param row_start: 起始行索引。
    :param row_end: 结束行索引。
    :param col_start: 起始列索引。
    :param col_end: 结束列索引。
    :param output_path: 输出的CSV路径。
    """
    # 选取指定范围的数据
    selected_data = df.iloc[row_start:row_end + 1, col_start:col_end + 1]

    # 准备要写入的数据
    # 首先添加索引信息
    indices_info = pd.DataFrame({
        'Row Start Index': [row_start],
        'Row End Index': [row_end],
        'Column Start Index': [col_start],
        'Column End Index': [col_end]
    })

    output_data = pd.concat([indices_info, selected_data.reset_index(drop=True)], ignore_index=True)

    output_data.to_csv(output_path, index=False)