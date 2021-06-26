import requests
from requests.auth import HTTPBasicAuth

class TestCookies():
	def test_header_cookie(self):
		url = "https://httpbin.testing-studio.com/cookies"
		header = {'Cookie':'TestCookie'}
		r = requests.get(url=url,headers=headers)
		print(r.request.headers)

	def test_cookies(self):
		url = "https://httpbin.testing-studio.com/cookies"
		cookies = dict(cookies_are='testcookies')
		r = requests.get(url=url, cookies=cookies)
		print(r.request.headers)

	def test_auth(self):
		url = "https://httpbin.testing-studio.com/basic-auth/apple/123123"
		r = requests.get("https://httpbin.testing-studio.com/basic-auth/apple/123123",auth=HTTPBasicAuth("apple","123123"))
		print(r.request.headers)
		print(r.text)







