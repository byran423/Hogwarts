from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchActions():
	def setup(self):
		option = webdriver.ChromeOptions()
		option.add_experimental_option('w3c',False)
		self.driver = webdriver.Chrome(options=option)

		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
	def teardown(self):
		self.driver.quit()

	def test_touchaction(self):
		"""
		打开百度，输入“selenium 搜索 点击搜索 拉到搜索结果最底部”

		"""
		self.driver.get('https://www.baidu.com/')
		el = self.driver.find_element_by_id('kw')
		el_search = self.driver.find_element_by_id('su')
		el.send_keys('selenium 测试')

		actions = TouchActions(self.driver)

		actions.tap(el_search)
		actions.perform()
		actions.scroll_from_element(el,0,10000).perform()
		# sleep(3)












