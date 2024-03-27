import os
import subprocess


folder_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\MFG'
dest_path = r'C:\Users\pengcheng.yan\Desktop\aps shaku\MFG_MJ6D'

for filename in os.listdir(folder_path):
    if (filename.endswith('.csv') and 'MJ6D' in filename and
            not ('InfinityDown' in filename) and not ('MacroUp' in filename) and not ('SuperMacroUp' in filename)):
        file_path = os.path.join(folder_path, filename)
        try:
            subprocess.run(f'copy "{file_path}" "{dest_path}"', shell=True)
        except Exception as e:
            print(f"Error occurred while copying {file_path}: {e}")