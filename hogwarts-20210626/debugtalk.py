import time

from httprunner import __version__
from httprunner.response import ResponseObject


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_folders_num(response: ResponseObject):
    print(response.resp_obj.json())
    folders = response.resp_obj.json()["data"]["folder"]
    return len(folders)
