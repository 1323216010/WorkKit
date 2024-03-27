import matplotlib.pyplot as plt


def float_line_img_multi(data_groups, cmap_name='hsv'):
    """
    data_groups: 一个列表，其中每个元素是一个字典，包含x, y数据和标签
                 例如: [{'x': [...], 'y': [...], 'tag': 'Label1'}, ...]
    cmap_name: 色彩映射的名称。
    """
    # 获取颜色映射
    cmap = plt.get_cmap(cmap_name)

    # 遍历所有数据组
    for i, group in enumerate(data_groups):
        x = group['x']
        y = group['y']
        tag = group['tag']

        # 根据数据组的索引和总数计算颜色
        color = cmap(float(i) / len(data_groups))

        # 将x, y根据x的值进行排序
        sorted_points = sorted(zip(x, y), key=lambda point: point[0])
        x_sorted, y_sorted = zip(*sorted_points)

        # 绘制散点图
        plt.scatter(x_sorted, y_sorted, s=5, marker='s', color=color, label=tag)

        # 绘制连线
        for j in range(len(x_sorted) - 1):
            if abs(x_sorted[j + 1] - x_sorted[j]) < 10:
                plt.plot([x_sorted[j], x_sorted[j + 1]], [y_sorted[j], y_sorted[j + 1]], color=color)

    # 添加图例
    plt.legend()

    # 添加网格线
    plt.grid(True, which='both', linestyle='--', linewidth=0.2)

    # 添加标题和坐标轴标签
    plt.title('Multiple Data Groups')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')

    plt.show()


# 示例使用
data_groups = [
    {'x': [1, 2, 3, 4], 'y': [10, 15, 13, 17], 'tag': 'Group 1'},
    {'x': [2, 3, 4, 5], 'y': [16, 5, 11, 9], 'tag': 'Group 2'}
]
float_line_img_multi(data_groups)
