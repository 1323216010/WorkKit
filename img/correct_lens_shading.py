import cv2
import numpy as np

def correct_lens_shading(img):
    height, width = img.shape[:2]
    # 生成中心到边缘的距离矩阵
    Y, X = np.ogrid[:height, :width]
    center = np.array([height//2, width//2])
    distance_from_center = np.sqrt((Y - center[0])**2 + (X - center[1])**2)
    # 标准化距离，使得最远处为1
    normalized_distance = distance_from_center / np.max(distance_from_center)
    # 根据距离调整亮度
    correction = 1 + 0.5 * normalized_distance  # 0.5是衰减系数，可以调整
    # 确保correction矩阵有与img相同的通道数
    correction = np.repeat(correction[:, :, np.newaxis], 3, axis=2)
    corrected_img = cv2.multiply(img.astype(np.float32), correction, dtype=cv2.CV_32F)  # 显式指定dtype
    return np.clip(corrected_img, 0, 255).astype(np.uint8)

img = cv2.imread('lens_shading.jpg')
corrected_img = correct_lens_shading(img)


# cv2.imshow('Original', img)
# cv2.imshow('Corrected', corrected_img)

cv2.imwrite('corrected_lens_shading.jpg', corrected_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
