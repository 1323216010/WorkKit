import os
import pandas as pd
import subprocess


def aps_online_list():
    list1 = []
    return list1


def read_csv(path):
    col_names = pd.read_csv(path, nrows=1).columns
    df = pd.read_csv(path, usecols=col_names, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def read_csv1(path, columns_to_read):
    # 首先读取列名，以确认文件中包含哪些列
    col_names = pd.read_csv(path, nrows=1).columns

    # 筛选出我们需要读取的列名
    valid_columns = [col for col in columns_to_read if col in col_names]

    # 读取特定的列
    df = pd.read_csv(path, usecols=valid_columns, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def find_files(path, include_list, exclude_list, file_types, depth=None, match_all_includes=False):
    result = []
    path_depth = len(path.rstrip(os.sep).split(os.sep))  # 获取初始路径的深度

    for root, dirs, files in os.walk(path):
        # 计算当前遍历的深度
        current_depth = len(root.rstrip(os.sep).split(os.sep))
        # 如果设置了深度，且当前深度超过初始路径深度加上设置的深度，则跳过
        if depth is not None and (current_depth - path_depth) >= depth:
            del dirs[:]  # 清空dirs列表，防止继续向下遍历
            continue

        for file in files:
            # 根据match_all_includes的值选择检查方式
            if match_all_includes:
                # 检查文件名是否包含include_list中的所有字符串
                if all(substr in file for substr in include_list):
                    if not any(substr in file for substr in exclude_list):
                        if any(file.endswith(ft) for ft in file_types):
                            result.append(os.path.join(root, file))
            else:
                # 检查文件名是否包含include_list中的任一字符串
                if any(substr in file for substr in include_list):
                    if not any(substr in file for substr in exclude_list):
                        if any(file.endswith(ft) for ft in file_types):
                            result.append(os.path.join(root, file))
    return result


def copy_files1(path, destination_folder):
    file_name = os.path.basename(path)
    dest_path = os.path.join(destination_folder, file_name)

    try:
        subprocess.run(f'copy "{path}" "{dest_path}"', shell=True)
    except Exception as e:
        print(f"Error occurred while copying {path}: {e}")