from appium.webdriver.common.mobileby import MobileBy

from test_app_work_wechat.po.add_member_page import AddMemberPage
from test_app_work_wechat.po.base_page import BasePage


class ContactPage(BasePage):
	ele_add_member = (MobileBy.XPATH, "//*[@text='添加成员']")

	def go_to_add_member(self):
		'''
		通讯录页面跳转到添加成员页面
		:return: 添加成员页面实例
		'''
		self.find(self.ele_add_member).click()

		return AddMemberPage(self.driver)

	# return

	def get_member_list(self):
		'''
		获取通讯录页面成员
		:return: 返回成员列表
		'''
		return []
