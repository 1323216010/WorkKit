import pandas as pd
import os


def add_duration_to_csvs(file_paths):
    for file_path in file_paths:
        # 确保文件存在
        if not os.path.exists(file_path):
            print(f"文件 {file_path} 不存在。")
            continue

        # 读取 CSV 文件
        df = pd.read_csv(file_path)

        # 检查 'PeakSearch_LowTemp' 列是否存在
        if 'PeakSearch_LowTemp' not in df.columns:
            print(f"文件 {file_path} 中不存在 'PeakSearch_LowTemp' 列。")
            continue

        # 计算 'duration' 列的值
        df['duration'] = df['PeakSearch_LowTemp'].apply(
            lambda x: x[-5:-1] if isinstance(x, str) and len(x) >= 5 else 'N/A')

        # 保存修改后的 DataFrame 到原 CSV 文件
        df.to_csv(file_path, index=False)
        print(f"已更新文件 {file_path}。")


file_paths = [
    r'C:\Users\pengcheng.yan\Desktop\peak search\C3051 search FineSearch.csv',
    r'C:\Users\pengcheng.yan\Desktop\peak search\C3052 search CoarseSearch.csv',
    r'C:\Users\pengcheng.yan\Desktop\peak search\C3052 search FineSearch.csv',
    r'C:\Users\pengcheng.yan\Desktop\peak search\C3059 search CoarseSearch.csv',
    r'C:\Users\pengcheng.yan\Desktop\peak search\C3059 search FineSearch.csv'
]

add_duration_to_csvs(file_paths)
