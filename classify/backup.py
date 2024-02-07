import os
import pandas as pd


directory = r'D:\data\VR_output'
for filename in os.listdir(directory):
    source_path = os.path.join(directory, filename)
    df = pd.read_csv(source_path)
    df.sort_values(by=['BARCODE', 'ITEM', 'time'], inplace=True)

    # 为每个BARCODE和ITEM组合生成ITEM_INDEX
    df['ITEM_INDEX'] = df.groupby(['BARCODE', 'ITEM']).cumcount() + 1

    df = df.sort_values(by=['BARCODE', 'ITEM', 'ITEM_INDEX'])
    df.to_csv(source_path, index=False)


