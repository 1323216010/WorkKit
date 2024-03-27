from bisect import bisect_right


def searchMatrix(matrix, target):
    col1 = [row[0] for row in matrix]
    row_index = bisect_right(col1, target) - 1

    if row_index < 0:
        return False

    # 在选定的行中使用二分搜索来查找target
    row = matrix[row_index]
    col_index = bisect_right(row, target) - 1

    if col_index < 0 or col_index >= len(row):
        return False
    return row[col_index] == target


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(searchMatrix(matrix, target))  # 应该输出True，因为3在矩阵中

    target = 13
    print(searchMatrix(matrix, target))  # 应该输出False，因为13不在矩阵中
