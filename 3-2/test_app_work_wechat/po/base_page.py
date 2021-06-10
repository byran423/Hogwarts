from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class BasePage():

	'''
	提供公共方法封装，即和页面无关的逻辑
	'''
	def __init__(self,best_driver=None):
		# 如果首次初始化，新建一个Webdriver
		if best_driver is None:
			desire_cap = {
				"platformName": "Android",
				# "deviceName": "860BDMM22KJX",
				"deviceName": "emulator-5554",
				"appPackage": "com.tencent.wework",
				"appActivity": ".launch.LaunchSplashActivity",
				"noReset": True,
				# 复用上次打开的app
				# "dontStopAppOnReset":True #
				# 跳过设备初始化，加快多用例运行速度
				"skipDeviceInitialization": True
			}
			self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)

		# 已经有Webdriver，不用再初始化
		else:
			self.driver:WebDriver = best_driver
		self.driver.implicitly_wait(10)

	def find(self, by, locator=None):
		if locator is None:
			# 如果入参是元祖(by, '')形式，解包
			return self.driver.find_element(*by)
			# 普通形式传参
		else:
			return self.driver.find_element(by, value=locator)










