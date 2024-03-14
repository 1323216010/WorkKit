import os
import hashlib
import pefile
from datetime import datetime

def get_file_info(file_path):
    try:
        # 获取文件基本信息
        file_size = os.path.getsize(file_path)
        modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

        # 计算文件的MD5哈希值
        with open(file_path, 'rb') as f:
            md5_hash = hashlib.md5()
            while chunk := f.read(8192):
                md5_hash.update(chunk)
            md5_digest = md5_hash.hexdigest()

        print(f"File: {file_path}")
        print(f"Size: {file_size} bytes")
        print(f"Last Modified: {modification_time}")
        print(f"MD5: {md5_digest}")

        # 分析PE文件信息
        if file_path.endswith('.exe') or file_path.endswith('.dll'):
            pe = pefile.PE(file_path)
            print(f"Number of Sections: {len(pe.sections)}")
            print(f"Compilation Time: {datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"EntryPoint: 0x{pe.OPTIONAL_HEADER.AddressOfEntryPoint:x}")
            print("Imported DLLs:")
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print(f"  - {entry.dll.decode()}")
        print("-" * 60)

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

file_paths = [
    "C:\\Windows\\SysWOW64\\winhaf9u.dll",
    "C:\\Windows\\SysWOW64\\winncap3x.dll",
    "C:\\Windows\\SysWOW64\\winoauv3.dll",
    "C:\\Windows\\SysWOW64\\winoav3.dll",
    "C:\\Windows\\SysWOW64\\winrdlv3.exe"
]

for path in file_paths:
    get_file_info(path)
