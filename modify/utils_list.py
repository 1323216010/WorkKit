import pandas as pd


def summary_cal():
    list1 = ['Barcode', 'swide_NTC_Temp']
    return list1



def summary_bank_all():
    list1 = ['barcode']
    bank_list = [f'#Bank{i}' for i in range(384)]
    list1 = list1 + bank_list
    return list1

def read_csv1(path, columns_to_read):
    # 首先读取列名，以确认文件中包含哪些列
    col_names = pd.read_csv(path, nrows=1).columns

    # 筛选出我们需要读取的列名
    valid_columns = [col for col in columns_to_read if col in col_names]

    # 读取特定的列
    df = pd.read_csv(path, usecols=valid_columns, low_memory=False, encoding="UTF-8", delimiter=',')
    return df