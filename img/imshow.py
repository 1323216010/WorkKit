import json
import cv2
import numpy as np
from tkinter import filedialog
from tkinter import Tk


def read_raw(filename, bits_num, width, height):
    with open(filename, 'rb') as file:
        if bits_num == 8:
            dtype = np.uint8
        elif bits_num in [10, 12, 16]:
            dtype = np.uint16
        else:
            raise ValueError("Unsupported bit depth")

        raw_data = np.fromfile(file, dtype=dtype)
        if len(raw_data) != width * height:
            raise ValueError("File size does not match specified dimensions")
        raw_data = np.reshape(raw_data, (width, height))
    return raw_data


def main():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    bits_num = config['bits_num']
    width = config['width']
    height = config['height']

    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Raw files", "*.raw")])
    if not file_path:
        print("No file selected")
        return

    raw_data = read_raw(file_path, bits_num, width, height)

    # Show the image
    cv2.imshow('Original', raw_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
