import pandas as pd
from pathlib import Path


def sum_counts_in_csv_files(directory):
    total_counts_sum = 0
    csv_files = Path(directory).glob('*.csv')

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)

        counts_sum = len(set(df['barcode'].tolist()))
        total_counts_sum += counts_sum
        print(f"{csv_file.name} has counts sum of {counts_sum}.")

    print(f"Total counts sum in all CSV files: {total_counts_sum}")


directory = r'C:\Users\pengcheng.yan\Desktop\compute'
sum_counts_in_csv_files(directory)
