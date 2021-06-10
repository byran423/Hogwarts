from time import sleep

from appium import webdriver


class TestBrowser():
	def setup(self):
		des_cap={
			'platformName':'android',
			'platformVersion':'6.0',
			'browserName':'Browser',
			'noRest':True,
			'deviceName':'emulator-5554'
		}
		self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_cap)
		self.driver.implicitly_wait(10)

	def teardown(self):
		self.driver.quit()

	def test_browser(self):
		self.driver.get('http://m.baidu.com')
		sleep(5)













