import matplotlib.pyplot as plt

# 假设 data 是一个包含浮点数的列表
data = [1.002, 1.003, 1.005, 1.006, 1.007, 1.005, 1.006, 1.007, 1.008]

# 创建一个更大的图形，以便更好地查看细节
plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(data, marker='o', linestyle='-', color='b')  # 'o' 表示点，'-' 表示实线

# 自定义图形以突出显示细微变化
plt.title('Float Data Line Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)  # 添加网格线
plt.tight_layout()  # 自动调整子图参数，以填充整个图形区域

# 显示图形
plt.show()
