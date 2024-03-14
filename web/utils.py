import os
import platform
import socket


def get_internal_ip():
    """获取本机内网 IP 地址"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 使用一个不存在的地址，目的是触发自动选择一个合适的内网 IP
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_info():
    info = {}

    # 获取内网IP
    try:
        info['ip'] = get_internal_ip()
    except Exception as e:
        info['ip'] = str(e)

    # 获取用户名
    try:
        info['username'] = os.getlogin()
    except Exception as e:
        info['username'] = str(e)

    # 获取系统信息
    try:
        info['system'] = platform.system()
    except Exception as e:
        info['system'] = str(e)

    # 获取系统版本
    try:
        info['version'] = platform.version()
    except Exception as e:
        info['version'] = str(e)

    # 获取用户主目录
    try:
        info['home_dir'] = os.path.expanduser('~')
    except Exception as e:
        info['home_dir'] = str(e)

    # 获取PATH环境变量
    try:
        info['path_env'] = os.environ.get('PATH')
    except Exception as e:
        info['path_env'] = str(e)

    # 获取FQDN
    try:
        info['fqdn'] = socket.getfqdn()
    except Exception as e:
        info['fqdn'] = str(e)

    return info
