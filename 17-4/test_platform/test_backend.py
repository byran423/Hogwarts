import requests as requests
from flask import request


def test_backend_testcase():
    url = "http://127.0.0.1:5000/testcase"
    data = {"name": "testcase1", "description": "abcd", "steps": ["a", "b", "c"]}
    res = requests.post(url, json=data)
    print(res.json())


def test_backend_testcase_orm():
    url = "http://127.0.0.1:5000/testcase_orm"
    data = {"name": "testcase1", "description": "abcd", "steps": ["a", "b", "c"]}
    res = requests.post(url, json=data)
    print(res.json())
