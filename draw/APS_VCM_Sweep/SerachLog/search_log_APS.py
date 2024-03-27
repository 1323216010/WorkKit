import json
import os
import sys
import pandas as pd
from utils import find_files_plus, merge_csv_with_path_list, copy_file_by_df, find_excel, search_aps_version


def main():
    sheet1 = pd.read_excel(find_excel('./')[0], sheet_name=0)
    list_vcmID = sheet1['vcmID'].tolist()

    sheet2 = pd.read_excel(find_excel('./')[0], sheet_name=1)
    with open('config/config_aps.json', 'r', encoding='utf-8') as file:
        list1 = json.load(file)

    for obj in list1:
        obj['path'] = sheet2[obj['type']].tolist()
        paths = find_files_plus(obj['path'], obj['excluded_folder'], obj['excluded_file'], obj['included_file'])
        df = merge_csv_with_path_list(paths, ['vcmID', 'time', 'Site'])
        df = df[df['vcmID'].isin(list_vcmID)]
        df['time'] = df['time'].str.replace('_', '')
        df['Site'] = df['Site'].str[-1]

        df.to_csv('APS' + '\\' + obj['type'] + '.csv', index=False)

        copy_file_by_df(df, obj['type'])


if __name__ == '__main__':
    search_aps_version()

    # 检查应用程序是否被打包
    if getattr(sys, 'frozen', False):
        # 如果应用程序被打包
        application_path = sys._MEIPASS
    else:
        # 如果应用程序未被打包
        application_path = os.path.dirname(os.path.abspath(__file__))

    try:
        main()
    except Exception as e:
        print(str(e))

    os.system("pause")



