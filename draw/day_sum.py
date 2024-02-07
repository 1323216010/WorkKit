import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter



df_pdx = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\PDX.csv')
df_vr = pd.read_csv(r'C:\Users\pengcheng.yan\Desktop\VR.csv')
df = pd.concat([df_pdx, df_vr])

df = df.groupby('day')['counts_sum'].sum().reset_index()
df['day'] = pd.to_datetime(df['day'])

# 按'day'列升序排序
df = df.sort_values('day')

df.to_csv(r'C:\Users\pengcheng.yan\Desktop\PDX and VR.csv', index=False)


# 将'day'列设置为索引
df.set_index('day', inplace=True)

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图形的大小
plt.plot(df.index, df['counts_sum'], marker='o', linestyle='-', color='b')  # 绘制折线图
plt.title('PDX And VR Counts Sum Over Time')  # 图表标题
plt.xlabel('Day')  # x轴标签
plt.ylabel('Counts Sum')  # y轴标签
plt.xticks(rotation=45)  # 旋转x轴上的标签，以便更容易阅读

# 创建一个ScalarFormatter对象，并设置不使用科学计数法
y_formatter = ScalarFormatter(useOffset=False)
y_formatter.set_scientific(False)

# 应用formatter到当前图表的y轴上
plt.gca().yaxis.set_major_formatter(y_formatter)

plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.show()  # 显示图表