from utils import get_info


info = get_info()
for key, value in info.items():
    print(f"{key}: {value}")