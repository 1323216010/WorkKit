import os
import pandas as pd
from pathlib import Path
import subprocess
import re


def find_files_plus(paths, excluded_dirs, excluded_files, included_files):
    target_files = []
    for path in paths:
        print('search:', path)
        # 遍历指定路径及其所有子目录
        for root, dirs, files in os.walk(path):
            # 在这里修改dirs列表，防止进一步遍历不需要的子目录
            dirs[:] = [d for d in dirs if all(sub not in d for sub in excluded_dirs)]

            # 过滤出不包含在excluded_files中的文件
            files = [f for f in files if all(sub not in f for sub in excluded_files)]
            # 过滤出包含在included_files中的文件
            files = [f for f in files if all(sub in f for sub in included_files)]

            print('search:', root)

            for file in files:
                target_files.append(os.path.join(root, file))

    return target_files


def merge_csv_with_path_list(file_paths, list1):
    dataframes = []

    for file_path in file_paths:
        try:
            df = read_csv1(file_path, list1)
            df.insert(0, 'path', file_path)
            dataframes.append(df)
        except Exception as e:
            print(str(e))

    all_df = pd.concat(dataframes, ignore_index=True)
    all_df = all_df.sort_values(by=list1[0])

    # 重置索引，并且不保留旧索引
    all_df = all_df.reset_index(drop=True)

    return all_df


def merge_csv_with_list(file_paths, list1, list_vcmID):
    dataframes = []

    for file_path in file_paths:
        try:
            df = read_csv1(file_path, list1)
            df = df[df['vcmID'].isin(list_vcmID)]
            df.insert(0, 'path', file_path)
            dataframes.append(df)
        except Exception as e:
            print(str(e))

    all_df = pd.concat(dataframes, ignore_index=True)
    all_df = all_df.sort_values(by=list1[0])

    # 重置索引，并且不保留旧索引
    all_df = all_df.reset_index(drop=True)

    return all_df


def read_csv(path):
    col_names = pd.read_csv(path, nrows=1).columns
    df = pd.read_csv(path, usecols=col_names, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def read_csv1(path, columns_to_read):
    # 首先读取列名，以确认文件中包含哪些列
    col_names = pd.read_csv(path, nrows=1, encoding="UTF-8").columns

    # 筛选出我们需要读取的列名
    valid_columns = [col for col in columns_to_read if col in col_names]

    # 读取特定的列
    df = pd.read_csv(path, usecols=valid_columns, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def copy_file_by_df(df, type):
    output_folder = 'APS' + '\\' + type
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, row in df.iterrows():
        path = Path(row['path'])
        folder = str(path.parent)
        vcmID = row['vcmID']
        time = row['time']
        folder = folder + '\\' + 'Debug_' + row['Site'] + '\\' + time
        file = find_files_plus([folder], ['Shaku', 'Result'], ['bin'], ['ApsCalibrationSweepFromMcu'])

        if file:
            output_path = output_folder + '\\' + vcmID
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            dest_path = copy_files(file[0], output_path)


def copy_files(path, destination_folder):
    file_name = os.path.basename(path)
    dest_path = os.path.join(destination_folder, file_name)

    try:
        subprocess.run(f'copy "{path}" "{dest_path}"', shell=True)
    except Exception as e:
        print(f"Error occurred while copying {path}: {e}")

    return dest_path


def find_excel(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith('xlsx'):
            source_path = os.path.join(directory, filename)
            files.append(source_path)

    return files


def summary_vcm():
    list1 = ['vcmID', 'global_time_stamp', 'PASS_FAIL', 'DCKEY']
    vcmUpDisplacement = [f'#vcmUpDisplacement_{i}' for i in range(96)]
    vcmUpAPSE = [f'#vcmUpAPSE_{i}' for i in range(96)]
    vcmUpAPSW = [f'#vcmUpAPSW_{i}' for i in range(96)]

    vcmUpCurrent = [f'#vcmUpCurrent_{i}' for i in range(96)]
    list1 = list1 + vcmUpDisplacement + vcmUpAPSE + vcmUpAPSW + vcmUpCurrent
    return list1


def traverse_ftu_vcm(df, type):
    output_folder = 'FTU' + '\\' + type
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, row in df.iterrows():
        vcmID = row['vcmID']
        DCKEY = row['DCKEY']

        list1 = []

        for index, value in row.items():
            get_vcm_data(list1, index, value)

        if len(list1) > 0:
            output_path = output_folder + '\\' + vcmID
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            df = pd.DataFrame(list1)
            df = df[['step'] + [col for col in df.columns if col != 'step']]

            df.to_csv(output_path + '\\' + vcmID + '_' + DCKEY + '.csv', index=False)


def get_vcm_data(list1, index, value):
    if 'vcmUpAPSE' in index or 'vcmUpAPSW' in index or 'vcmUpCurrent' in index or 'vcmUpDisplacement' in index:
        while len(list1) <= int(get_index(index)):
            list1.append({})

        list1[int(get_index(index))][replace_num(index)] = value
        list1[int(get_index(index))]['step'] = int(get_index(index))


def replace_num(original_string):
    modified_string = re.sub(r'_[0-9]+$', '', original_string)

    return modified_string


def get_index(original_string):
    # 使用split方法以'_'为分隔符分割字符串
    parts = original_string.split('_')
    # 获取最后一个分割后的元素
    substring_after_underscore = parts[-1]
    return substring_after_underscore


def search_aps_version():
    print('Search_APS_Log version is 20240326a')
    print("Update Log")
    print("=========================================")
    print("[2024-03-26]")
    print("-----------------------------------------")
    print("Features:")
    print("    - Supports fast search of APS VCM Sweep data.")
    print()
    print("For any questions or concerns, please contact:")
    print("Pengcheng.yan@cowellchina.com")
    print("=========================================")


def search_ftu_version():
    print('Search_FTU_Log version is 20240326a')
    print("Update Log")
    print("=========================================")
    print("[2024-03-26]")
    print("-----------------------------------------")
    print("Features:")
    print("    - Supports vertical expansion of FTU VCM Sweep data.")
    print()
    print("For any questions or concerns, please contact:")
    print("Pengcheng.yan@cowellchina.com")
    print("=========================================")


def data_visualizer_version():
    print('Data Visualizer version is 20240326a')
    print("Update Log")
    print("=========================================")
    print("[2024-03-26]")
    print("-----------------------------------------")
    print("Features:")
    print("    - Support arbitrary specified data plotting.")
    print()
    print("For any questions or concerns, please contact:")
    print("Pengcheng.yan@cowellchina.com")
    print("=========================================")