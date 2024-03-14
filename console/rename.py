import os

def rename_file(original_filename, new_filename):
    try:
        os.rename(original_filename, new_filename)
        print(f"File renamed from '{original_filename}' to '{new_filename}'")
    except OSError as e:
        print(f"Error: {e}")


original_filename = 'C:\\Windows\\SysWOW64\\Winrdlv3.exe'
new_filename = 'C:\\Users\\pengcheng.yan\\Desktop\\test\\Winrdlv31.exe'
rename_file(original_filename, new_filename)
