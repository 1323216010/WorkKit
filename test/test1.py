import os
import time

# 要监视的目录
WATCH_PATH = r'C:\Users\pengcheng.yan\Desktop\test'

# 上次访问的文件状态
last_files = {}


# 初始化或更新目录下的文件状态
def update_files_status():
    global last_files
    current_files = {f: os.path.getmtime(os.path.join(WATCH_PATH, f)) for f in os.listdir(WATCH_PATH)}
    added = current_files.keys() - last_files.keys()
    removed = last_files.keys() - current_files.keys()
    modified = {f for f in last_files if f in current_files and last_files[f] != current_files[f]}
    last_files = current_files
    return added, removed, modified


def monitor():
    while True:
        added, removed, modified = update_files_status()
        if added:
            print(f"Added files: {added}")
        if removed:
            print(f"Removed files: {removed}")
        if modified:
            print(f"Modified files: {modified}")

        time.sleep(0.001)


if __name__ == "__main__":
    monitor()
