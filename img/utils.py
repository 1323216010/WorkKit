import numpy as np


def read_raw_image(file_path, width, height, bit_depth=8):
    dtype = np.uint8 if bit_depth == 8 else np.uint16
    with open(file_path, 'rb') as file:
        img_array = np.frombuffer(file.read(), dtype=dtype)
        img_array = img_array.reshape((height, width))
    return img_array
