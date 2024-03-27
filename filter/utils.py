import os
import csv
import pandas as pd

def find_files_with_list(paths, include_list, exclude_list, file_types, depth=None, match_all_includes=False):
    result = []

    for path in paths:  # 遍历路径列表
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

def find_matching_records(csv_file, criteria):
    """
    读取CSV文件，返回所有符合给定条件的行。

    :param csv_file: CSV文件的路径。
    :param criteria: 一个字典，包含需要匹配的键值对。
    :return: 符合条件的行的列表。
    """
    matching_rows = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if all(row.get(key) == value for key, value in criteria.items()):
                matching_rows.append(row)

    return matching_rows

def find_matching_list(csv_file, criteria):
    list1 = find_matching_records(csv_file, criteria)
    list2 = []
    for row in list1:
        dict1 = {}
        dict1['vcm_ID'] = row['vcm_ID']
        dict1['site'] = row['Site'][-1]
        dict1['time'] = row["time"].replace("_", "")
        dict1['path'] = csv_file
        list2.append(dict1)
    return list2


def filter_dataframe_by_criteria(df, criteria):
    """
    在DataFrame中查找所有符合给定条件的行。

    :param df: 要搜索的 pandas DataFrame。
    :param criteria: 一个字典，包含需要匹配的键值对。
    :return: 一个DataFrame，包含所有符合条件的行。
    """
    # 使用 criteria 字典构建一个条件表达式
    condition = pd.Series([True] * len(df))
    for key, value in criteria.items():
        condition &= (df[key] == value)

    # 应用条件表达式并返回匹配的行
    return df[condition]

def find_records(csv_file, field_name):
    """
    读取CSV文件，返回一个字典，该字典包含指定字段名和对应的值。

    :param csv_file: CSV文件的路径。
    :param field_name: 需要提取值的字段名称。
    :return: 包含指定字段名和对应值的字典。
    """
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # 读取第二行，即数据行
        row = next(reader, None)
        if row and field_name in row:
            return {field_name: row[field_name]}
        else:
            return {field_name: None}  # 如果没有找到字段或者没有数据行，返回None

def merge_csv_files(file_paths):
    # 创建一个空的DataFrame作为初始数据集
    merged_data = pd.DataFrame()

    # 遍历文件路径列表
    for file in file_paths:
        try:
            # 读取每个CSV文件，将所有列作为字符串类型读取
            data = pd.read_csv(file, dtype=str)
            # 将读取的数据追加到merged_data
            merged_data = pd.concat([merged_data, data], ignore_index=True)
        except:
            print('error file', file)

    return merged_data

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def delete_file_if_exists(file_path):
    # 检查文件是否存在
    if os.path.isfile(file_path):
        try:
            # 如果文件存在，尝试删除它
            os.remove(file_path)
            print(f"File {file_path} has been deleted.")
        except OSError as e:
            # 如果删除过程中出现错误，打印错误信息
            print(f"Failed to delete file {file_path}. Error message: {e}")
    else:
        # 如果文件不存在，打印信息
        print(f"File {file_path} does not exist.")

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

def filter_files(file_paths, start_str):
    """
    过滤掉文件名不以指定字符串开头的文件路径。

    :param file_paths: 文件路径列表
    :param start_str: 用于过滤的起始字符串
    :return: 过滤后的文件路径列表
    """
    return [path for path in file_paths if os.path.basename(path).startswith(start_str)]



def get_value_from_csv(x, y, csv_path):
    df = pd.read_csv(csv_path)
    # 获取第x列第y行的值
    # 注意pandas的索引是从0开始的，如果输入的x和y是从1开始计数的，需要相应地调整
    value = df.iloc[y - 1, x - 1]  # 如果x和y是基于1的索引，减1进行调整
    return value


def summary_bank():
    list1 = []

    bank = [f'#Bank{i}' for i in range(1024)]

    list1 = list1 + bank
    return list1

