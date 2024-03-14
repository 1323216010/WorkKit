import os, sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from utils import read_csv1, summary_list
from generate_pdf import generate, generate1


dict1 = {}

def main():
    folder_path = input("Please enter the file path: ")

    img_path = 'img'

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    pdf = canvas.Canvas('Laser_AF_Z_um and AF_Z.pdf')

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

    pdf1 = canvas.Canvas('AF_current_DAC.pdf')
    generate1(pdf1, list_dict, img_path)
    pdf1.save()
    print("The task is complete.")


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

    try:
        main()
    except Exception as e:
        print(str(e))

    os.system("pause")

