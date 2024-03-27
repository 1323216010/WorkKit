from utils import read_csv
import os


folder_path = r'C:\Users\pengcheng.yan\Desktop\1_C2_DPC_Simulation'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = read_csv(file_path)
        df['time'] = df['time'].str.replace('/', '_').str.replace(' ', '_').str.replace('-', '_')
        df.to_csv(file_path, index=False)



