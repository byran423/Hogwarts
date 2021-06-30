import time

from httprunner import __version__
from httprunner.response import ResponseObject
import hashlib


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_token(phone, password, timestamp):
    s = "".join([phone, password, str(timestamp)])
    token = hashlib.md5(s.encode("utf-8")).hexdigest()
    print(token)
    return token


def get_folders_num(response: ResponseObject):
    print(response.resp_obj.json())
    folders = response.resp_obj.json()["data"]["folder"]
    return len(folders)
