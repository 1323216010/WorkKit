import os, json
import pandas as pd
from utils import save_range_to_csv


with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

folder_path = input("Please enter the file path: ")

if not os.path.exists('out'):
    os.makedirs('out')

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        df = pd.read_csv(file_path, header=None)

        # 确保x1 < x2 和 y1 < y2，这样就能正确地定义矩形区域
        x1, x2 = sorted([config['p1'][0], config['p2'][0]])
        y1, y2 = sorted([config['p1'][1], config['p2'][1]])

        # 使用iloc选择矩形区域的数据
        # rectangle_data = df.iloc[y1:y2 + 1, x1:x2 + 1]

        output_path = './out/' + filename.replace(".csv", "") + "_(" + str(x1) + "," + str(y1) + ")" + "~" + "(" + str(x2) + "," + str(y2) + ")" + ".csv"

        save_range_to_csv(df, x1, x2, y1, y2, output_path)


