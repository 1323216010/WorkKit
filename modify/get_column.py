import os
import pandas as pd
from utils_list import summary_bank_all, read_csv1, summary_cal


folder_path = r'C:\Users\pengcheng.yan\Desktop\NTC temp\rawlog\3Sweeps'
output_path = r'C:\Users\pengcheng.yan\Desktop\test_log\sweep_doe1'

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = read_csv1(file_path, summary_cal())

        df = df.iloc[0:1]

        output_file_path = os.path.join(output_path, f"{os.path.splitext(filename)[0]}.csv")

        df.to_csv(output_file_path, index=False)


