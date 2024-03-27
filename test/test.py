import numpy as np

def calculate_r_squared(x, y):
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    if x.shape[0] != y.shape[0]:
        raise ValueError("Input arrays should have the same number of samples.")

    if x.shape[0] < 2:
        raise ValueError("Not enough data points to perform regression.")

    if len(x.shape) == 1:
        x = x.reshape(-1, 1)

    # 构造设计矩阵 X，第一列是1（对应截距b），第二列是x值（对应斜率a）
    X = np.c_[np.ones(x.shape[0]), x]

    # 使用最小二乘法计算回归系数 beta
    beta = np.linalg.pinv(X.T @ X) @ X.T @ y

    # 分解 beta 为截距 b 和斜率 a
    b = beta[0]
    a = beta[1:]

    # 计算 y 的预测值 y_pred
    y_pred = X @ beta

    # 计算总平方和 TSS 和残差平方和 ESS
    TSS = np.sum((y - np.mean(y)) ** 2)
    ESS = np.sum((y - y_pred) ** 2)

    # 计算 R-squared r2
    epsilon = 1e-10
    if TSS < epsilon:
        r2 = 1
    else:
        r2 = 1 - (ESS / TSS)

    return r2, a, b, y_pred

x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

r_squared, slope, intercept, y_predicted = calculate_r_squared(x_data, y_data)


print("R-squared:", r_squared)
print("Slope:", slope)
print("Intercept:", intercept)
print("Predicted y values:", y_predicted)