import pandas as pd
from utils import find_files, summary_cal, read_csv1, copy_files1



df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\doe shaku\abcd.csv')
for index, row in df.iterrows():
    barcode = row['barcode']
    time = row['time']
    time = time.replace('_', '')
    files = find_files(r'C:\Users\pengcheng.yan\Desktop\doe shaku\por',
                       [barcode, str(time), 'ShakuInput_shaku_A'], [], ['.csv'], match_all_includes=True)

    try:
        copy_files1(files[0], r'C:\Users\pengcheng.yan\Desktop\doe shaku\por1')
    except Exception as e:
        print(str(e))

    # sweep_df = read_csv1(files[0], summary_cal())
    # sweep_df.to_csv(files[0], index=False)
