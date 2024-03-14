import os
import csv
import pandas as pd

def get_value_from_csv(x, y, csv_path):
    df = pd.read_csv(csv_path)
    # 获取第x列第y行的值
    # 注意pandas的索引是从0开始的，如果输入的x和y是从1开始计数的，需要相应地调整
    value = df.iloc[y - 1, x - 1]  # 如果x和y是基于1的索引，减1进行调整
    return value


get_value_from_csv()