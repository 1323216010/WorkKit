import pandas as pd

def extract_datetime(realpath):
    # 假设时间总是位于倒数第二个下划线后
    try:
        datetime_str = realpath.split('_')[-2] + '_' + realpath.split('_')[-1].split('.')[0]
        return pd.to_datetime(datetime_str, format='%Y%m%d_%H%M%S')
    except ValueError:
        return pd.NaT  # 如果转换失败，返回NaT

# 示例用法
realpath = "FTU_20231013_051124_NULL_F0W3424004G05KR1J_Dark-D_TempNoise5-ModeD1-OPB_20231013_051330.raw"
print(extract_datetime(realpath))