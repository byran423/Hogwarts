import requests
from jsonpath import jsonpath
from requests import request
from requests_xml import XMLSession
from hamcrest import *

class TestJsonPath:
	def test_json_path(self):
		url = "https://ceshiren.com/categories.json"
		r = requests.get(url)
		print(r.text+'-----------------')
		print(r.json())
		assert r.status_code == 200
		# jsonpath 传递需要json obj
		assert jsonpath(r.json(),'$..name')[0] == '开源项目'

	def test_hamcrest(self):
		url = "https://ceshiren.com/categories.json"
		r = requests.get(url)
		print(r.text + '-----------------')
		print(r.json())
		assert r.status_code == 200
		# jsonpath 传递需要json obj
		assert_that(jsonpath(r.json(),'$..name')[0], equal_to('开源项目'))














