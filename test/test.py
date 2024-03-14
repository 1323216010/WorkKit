import cv2
import numpy as np
from tkinter import filedialog
from tkinter import Tk


def read_raw(filename, bits_num, rows, cols):
    with open(filename, 'rb') as file:
        if bits_num == 8:
            dtype = np.uint8
        elif bits_num in [10, 12, 16]:
            dtype = np.uint16
        else:
            raise ValueError("Unsupported bit depth")

        raw_data = np.fromfile(file, dtype=dtype)
        if len(raw_data) != rows * cols:
            raise ValueError("File size does not match specified dimensions")
        raw_data = np.reshape(raw_data, (rows, cols))
    return raw_data


def demosaic_RGGB_to_RGB(raw_data):
    # Assuming raw_data is of 'RGGB' Bayer pattern
    # Convert raw_data to a 3-channel BGR image using demosaicing
    color_image = cv2.cvtColor(raw_data, cv2.COLOR_BayerBG2BGR)
    return color_image


def main():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Raw files", "*.raw")])
    if not file_path:
        print("No file selected")
        return

    bits_num = 8  # or 10, 12, 16 depending on your file
    rows = 4208
    cols = 3120
    raw_data = read_raw(file_path, bits_num, rows, cols)
    color_image = demosaic_RGGB_to_RGB(raw_data)

    # Show the color image
    cv2.imshow('Demosaiced', color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
