import os
import pandas as pd


folder_path = r'C:\Users\pengcheng.yan\Desktop\PD40116-LGD020\POR'
output_path = r'C:\Users\pengcheng.yan\Desktop\PD40116-LGD020\DOE'

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        df['Laser_Displacement2'] = df['Laser_Displacement2'] + 7


        output_file_path = os.path.join(output_path, filename)
        df.to_csv(output_file_path, index=False)


