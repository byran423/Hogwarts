from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():

	_base_url = ''
	'''
	BasePage 提供公共方法封装，即和页面逻辑无关的封装
	比如解决driver初始化的问题
	'''
	def __init__(self,best_driver=None):
		if best_driver is None:

			#  复用浏览器
			chrome_arg = webdriver.ChromeOptions()
			chrome_arg.debugger_address = '127.0.0.1:9222'
			self.driver = webdriver.Chrome(options=chrome_arg)
			self.driver.get(self.base_url)
		else:
			# 添加一个WebDriver类型注解，解决类型提示的问题
			self.driver:WebDriver = best_driver
		# 打开首页

		self.driver.implicitly_wait(5)

	def find(self, by, locator=None):
		# 如果只穿入一个元祖参数
		if locator is None:
			return self.driver.find_element(*by)
		# 如果传入正常的两个参数
		else:
			return self.driver.find_element(by,value=locator)











