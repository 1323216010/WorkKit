import pandas as pd
import re


summary_df = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\test5\item_counts_summary.csv')

# 定义一个函数来截断-符号后紧接数字的ITEM
def truncate_item(item):
    # 查找-后直接跟随数字的模式，并截断
    truncated = re.sub(r'-\d.*', '', item)
    return truncated

# 应用该函数到ITEM列
summary_df['Truncated_ITEM'] = summary_df['ITEM'].apply(truncate_item)

# 对截断后的ITEM进行分组，合计相关列
aggregated_df = summary_df.groupby('Truncated_ITEM').agg({
    'Total_Counts': 'sum',
    'Counts_Under_20': 'sum',
    'Counts_Over_20': 'sum',
    'Counts_Over_50': 'sum',
    'Counts_Over_100': 'sum'
}).reset_index()


aggregated_df.to_csv('item_counts_summary.csv', index=False)
