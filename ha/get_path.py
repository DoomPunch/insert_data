import sys


def get_config_path(relate_path):
    a = sys.path[0].split('\\')
    a = a[:len(a)]
    a.append(relate_path)
    config_path = '/'.join(a)
    return config_path
