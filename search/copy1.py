import os
import json
from utils import copy_files1, copy_files_with_json


with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


json_file = config['paths']
destination_folder = config['out_path']

copy_files_with_json(json_file, destination_folder)

os.system("pause")
