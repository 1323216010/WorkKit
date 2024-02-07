import pandas as pd
from pathlib import Path

def sum_counts_in_csv_files(directory):
    total_counts_sum = 0
    csv_files = Path(directory).glob('*.csv')

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        counts_sum = df['counts'].sum()  # 计算当前文件的counts列的总和
        total_counts_sum += counts_sum  # 累加到总和中
        print(f"{csv_file.name} has counts sum of {counts_sum}.")

    print(f"Total counts sum in all CSV files: {total_counts_sum}")

directory = r'D:\data\VR_output_day_count'
sum_counts_in_csv_files(directory)
