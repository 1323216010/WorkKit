from  draw import float_line_img, float_overlay_line_img


def generate(pdf, list_dict, img_path):
    img_w, img_h = 640, 480
    pdf_size = (1920, 1080)
    pdf.setPageSize(pdf_size)
    pdf.setFont('yan', 17)

    flag = 1
    for dict1 in list_dict:
        float_line_img(dict1['df']['Laser_AF_Z_um'].tolist(), dict1['id'], img_path, '_Laser_AF_Z_um')
        float_line_img(dict1['df']['AF_Z'].tolist(), dict1['id'], img_path, '_AF_Z')

        img_x = 320
        if (flag):
            img_y = 60 + img_h
            flag = 0
        else:
            img_y = 60
            flag = 1

        dict1["font_high"] = 20
        pdf.drawImage(img_path + '/' + dict1['id'] + '_Laser_AF_Z_um.png', img_x, img_y, img_w, img_h)
        text_width = pdf.stringWidth(dict1['id'] + '', 'yan', 17)
        pdf.drawString(320 + (img_w - text_width) / 2, img_h + img_y - 25 + dict1["font_high"], dict1['id'] + '_Laser_AF_Z_um')

        img_x = 320 + img_w
        pdf.drawImage(img_path + '/' + dict1['id'] + '_AF_Z.png', img_x, img_y, img_w, img_h)
        text_width = pdf.stringWidth(dict1['id'] + '_AF_Z', 'yan', 17)
        pdf.drawString(320 + img_w + (img_w - text_width) / 2, img_h + img_y - 25 + dict1["font_high"], dict1['id'] + '_AF_Z')

        if (flag == 1):
            pdf.showPage()
            pdf.setFont('yan', 17)


def generate1(pdf, list_dict, img_path):
    img_w, img_h = 640, 480
    pdf_size = (1920, 1080)
    pdf.setPageSize(pdf_size)
    pdf.setFont('yan', 17)

    flag = True
    x_flag = 0
    for dict1 in list_dict:
        float_line_img(dict1['df']['AF_current_DAC'].tolist(), dict1['id'], img_path, '_AF_current_DAC')

        img_x = 320
        if (flag):
            img_y = 60 + img_h
        else:
            img_y = 60

        dict1["font_high"] = 20

        if x_flag == 0:
            pdf.drawImage(img_path + '/' + dict1['id'] + '_AF_current_DAC.png', img_x, img_y, img_w, img_h)
            text_width = pdf.stringWidth(dict1['id'] + '_AF_current_DAC', 'yan', 17)
            pdf.drawString(320 + (img_w - text_width) / 2, img_h + img_y - 25 + dict1["font_high"],
                           dict1['id'] + '_Laser_AF_Z_um')
            x_flag = 1
        else:
            img_x = 320 + img_w
            pdf.drawImage(img_path + '/' + dict1['id'] + '_AF_current_DAC.png', img_x, img_y, img_w, img_h)
            text_width = pdf.stringWidth(dict1['id'] + '_AF_current_DAC', 'yan', 17)
            pdf.drawString(320 + img_w + (img_w - text_width) / 2, img_h + img_y - 25 + dict1["font_high"],
                           dict1['id'] + '_AF_current_DAC')
            x_flag = 0
            flag = not flag


        if (flag and x_flag == 0):
            pdf.showPage()
            pdf.setFont('yan', 17)


