import cv2
import numpy as np


def correct_color_shading(img):
    correction_blue = np.linspace(1.0, 0.8, img.shape[1])  # 从左到右，蓝色通道亮度逐渐减小
    correction_red = np.linspace(0.8, 1.0, img.shape[1])  # 从左到右，红色通道亮度逐渐增加

    # 对蓝色和红色通道应用校正
    img[:, :, 0] = cv2.multiply(img[:, :, 0].astype(np.float32), correction_blue)
    img[:, :, 2] = cv2.multiply(img[:, :, 2].astype(np.float32), correction_red)

    return np.clip(img, 0, 255).astype(np.uint8)



img = cv2.imread('path_to_your_image.jpg')
corrected_img = correct_color_shading(img)

cv2.imshow('Original', img)
cv2.imshow('Corrected for Color Shading', corrected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
