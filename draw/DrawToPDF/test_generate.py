import os, sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from utils import read_csv1, summary_list
from generate_pdf import generate


dict1 = {}

def main():
    folder_path = r'C:\Users\pengcheng.yan\Desktop\test'

    img_path = 'img_test'

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    pdf = canvas.Canvas('summary_test.pdf')

    list_dict = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = read_csv1(file_path, summary_list())

            list1 = filename.split("_")
            sensor_id = list1[-3]
            time = list1[-2] + list1[-1].split(".")[0]
            id = sensor_id + '_' + time

            list_dict.append({'df': df, 'id': id})

    generate(pdf, list_dict, img_path)
    pdf.save()


if __name__ == '__main__':

    # 检查应用程序是否被打包
    if getattr(sys, 'frozen', False):
        # 如果应用程序被打包
        application_path = sys._MEIPASS
    else:
        # 如果应用程序未被打包
        application_path = os.path.dirname(os.path.abspath(__file__))

    ttf_path = os.path.join(application_path, 'ttf', 'DejaVuSans.ttf')

    pdfmetrics.registerFont(TTFont('yan', ttf_path))

    main()
