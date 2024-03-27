import pandas as pd


path = r'C:\Users\pengcheng.yan\Desktop\OQC APS Cal\results.csv'
df = pd.read_csv(path)


def extract_vcmID(sn):
    parts = sn.split('_')
    if len(parts) > 3:
        return parts[3]  # 返回第三个下划线到第四个下划线之间的子串
    else:
        return ''  # 如果格式不正确，返回空字符串


df['vcmID'] = df['SN'].apply(extract_vcmID)
df = df[['vcmID'] + [col for col in df.columns if col != 'vcmID']]

df.to_csv(path, index=False)
