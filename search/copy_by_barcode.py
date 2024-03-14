import pandas as pd
from utils import find_files, summary_cal, read_csv1, copy_files1



df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\test_log\500pcs_por.csv')
for index, row in df.iterrows():
    barcode = row['barcode']
    time = row['time']
    time = time.replace('_', '')
    files = find_files(r'C:\Users\pengcheng.yan\Desktop\NTC temp\por_sweep',
                       [barcode, str(time), 'ApsCalibrationSweepFromMcu'], [], ['.csv'], match_all_includes=True)

    copy_files1(files[0], r'C:\Users\pengcheng.yan\Desktop\test_log\sweep_por')
    # sweep_df = read_csv1(files[0], summary_cal())
    # sweep_df.to_csv(files[0], index=False)
