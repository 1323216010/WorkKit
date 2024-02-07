import os
import pandas as pd


directory = r'D:\data\PDX'

for filename in os.listdir(directory):
    try:
        source_path = os.path.join(directory, filename)
        df = pd.read_csv(source_path)
    except Exception as e:
        print('Error Message: ', str(e))
        print(source_path)