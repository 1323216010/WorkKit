import os
import matplotlib.pyplot as plt
from utils import read_csv


def float_img(picture, items, vcmID):
    data_groups = []
    for obj in items:
        directory = '.' + obj['path'] + '/' + vcmID
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                source_path = os.path.join(directory, filename)
                df = read_csv(source_path)
                dict1 = {}
                dict1['tag'] = obj['tag']
                dict1['x'] = df[obj['x']].tolist()
                dict1['y'] = df[obj['y']].tolist()
                data_groups.append(dict1)
                break

    float_line_img_multi(data_groups, picture, vcmID)

    return dict1


def float_line_img_multi(data_groups, picture, vcmID, cmap_name='hsv'):
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

    # 初始化最小和最大值
    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')
    for group in data_groups:
        x_min = min(x_min, min(group['x']))
        x_max = max(x_max, max(group['x']))
        y_min = min(y_min, min(group['y']))
        y_max = max(y_max, max(group['y']))

    # 计算最小和最大值
    x_min = x_min * 0.9 if x_min < -150 else int(picture['x_min'])
    x_max = x_max * 1.1 if x_max > 150 else int(picture['x_max'])

    y_min = y_min * 0.9 if y_min < -1500 else int(picture['y_min'])
    y_max = y_max * 1.1 if y_max > 1500 else int(picture['y_max'])

    # 设置x和y轴的最小和最大范围
    plt.xlim([x_min, x_max])
    plt.ylim([y_min, y_max])

    # 添加图例
    plt.legend()

    # 添加网格线
    plt.grid(True, which='both', linestyle='--', linewidth=0.2)

    # 添加标题和坐标轴标签
    plt.title(picture['title'] + '\n' + 'VCM ID: ' + vcmID)
    plt.xlabel(picture['xlabel'])
    plt.ylabel(picture['ylabel'])

    plt.savefig('./images/' + picture['title'] + '/' + picture['title'] + ' ' + vcmID + '.png', dpi=250)

    # 清理当前的plt环境，避免后续绘图受到影响
    plt.clf()
    plt.close()

    # plt.show()
