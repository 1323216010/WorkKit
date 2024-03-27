import os, sys, json
import pandas as pd
from utils import find_excel, data_visualizer_version
from draw import float_img


def main():
    sheet1 = pd.read_excel(find_excel('./')[0], sheet_name=0)
    list_vcmID = sheet1['vcmID'].tolist()

    with open('config/config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    list1 = config['pictures']

    if not os.path.exists('images'):
        os.makedirs('images')

    for vcmID in list_vcmID:
        for obj in list1:
            if not os.path.exists('images/' + obj['title']):
                os.makedirs('images/' + obj['title'])

            items = obj['items']
            dict1 = float_img(obj, items, vcmID)


if __name__ == '__main__':
    data_visualizer_version()
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




