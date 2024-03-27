import os
import json
import pandas as pd
from pathlib import Path
import shutil
import subprocess


def summary_cal():
    list1 = ['Barcode', 'swide_NTC_Temp']
    return list1


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


def copy_files(json_file, destination_folder):
    destination_folder = Path(destination_folder)
    if not destination_folder.exists():
        destination_folder.mkdir(parents=True)

    with open(json_file, 'r', encoding='utf-8') as file:
        file_paths = json.load(file)

    for file_path in file_paths:
        source_path = Path(file_path)
        if source_path.is_file():
            dest_path = destination_folder / source_path.name
            try:
                shutil.copy(source_path, dest_path)
            except Exception as e:
                print(f"Failed to copy {source_path} to {dest_path}: {e}")
        else:
            print(f"File not found or is not a file: {source_path}")


def copy_files_with_json(json_file, destination_folder):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 读取JSON文件中的路径列表
    with open(json_file, 'r', encoding='utf-8') as file:
        file_paths = json.load(file)

    # 遍历列表中的每个文件路径
    for path in file_paths:
        # 构建目标文件路径
        file_name = os.path.basename(path)
        dest_path = os.path.join(destination_folder, file_name)

        try:
            subprocess.run(f'copy "{path}" "{dest_path}"', shell=True)
        except Exception as e:
            print(f"Error occurred while copying {path}: {e}")

def read_csv(path):
    col_names = pd.read_csv(path, nrows=1).columns
    df = pd.read_csv(path, usecols=col_names, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def find_files_plus(paths, excluded_dirs, excluded_files, included_files):
    target_files = []
    for path in paths:
        # 遍历指定路径及其所有子目录
        for root, dirs, files in os.walk(path):
            # 在这里修改dirs列表，防止进一步遍历不需要的子目录
            dirs[:] = [d for d in dirs if all(sub not in d for sub in excluded_dirs)]

            # 过滤出不包含在excluded_files中的文件
            files = [f for f in files if all(sub not in f for sub in excluded_files)]
            # 过滤出包含在included_files中的文件
            files = [f for f in files if all(sub in f for sub in included_files)]

            for file in files:
                target_files.append(os.path.join(root, file))

    return target_files
