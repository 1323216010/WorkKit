import pandas as pd
from pathlib import Path

def count_csv_rows(directory):
    total_rows = 0
    csv_files = Path(directory).glob('*.csv')

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        rows = len(df)
        total_rows += rows
        print(f"{csv_file.name} has {rows} rows.")

    print(f"Total rows in all CSV files: {total_rows}")


directory = r'D:\data\PDX'
count_csv_rows(directory)
