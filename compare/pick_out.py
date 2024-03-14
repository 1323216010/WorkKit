import json
import pandas as pd
from utils_search import compile_patterns, save_list_as_json


df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\log\doe summary log.csv')
patterns = df['barcode'].tolist()

regex = compile_patterns(patterns)  # 编译成一个正则表达式

list1 = []

with open('por_paths.json', 'r', encoding='utf-8') as f:
    files = json.load(f)


# 检查当前目录中的文件
for file in files:
    # 使用正则表达式来检查文件名是否包含patterns中的任意一个
    if regex.search(file):
        # 如果包含，将路径和文件名添加到list1中
        list1.append(file)

save_list_as_json(list1, 'list1.json')