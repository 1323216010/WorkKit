import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

def summary_list():
    list1 = ['Laser_AF_Z_um', 'AF_Z', 'AF_current_DAC']

    return list1

def read_csv1(path, columns_to_read):
    # 首先读取列名，以确认文件中包含哪些列
    col_names = pd.read_csv(path, nrows=1).columns

    # 筛选出我们需要读取的列名
    valid_columns = [col for col in columns_to_read if col in col_names]

    # 读取特定的列
    df = pd.read_csv(path, usecols=valid_columns, low_memory=False, encoding="UTF-8", delimiter=',')
    return df



