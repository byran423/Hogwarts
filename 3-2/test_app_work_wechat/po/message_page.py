from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_app_work_wechat.po.base_page import BasePage
from test_app_work_wechat.po.contact_page import ContactPage


class MessagePage(BasePage):
	ele_contact = (MobileBy.XPATH, '//*[@text="通讯录"]')

	def go_to_contact(self):
		'''
		消息页面，跳转到通讯录页面
		:return: 返回通讯录页面实例
		'''

		# self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]')
		self.find(self.ele_contact).click()
		return ContactPage(self.driver)
	# return
