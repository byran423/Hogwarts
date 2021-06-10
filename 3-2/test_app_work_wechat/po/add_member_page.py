from appium.webdriver.common.mobileby import MobileBy

from test_app_work_wechat.po.base_page import BasePage

from test_app_work_wechat.po.manual_input_add_member_page import ManualInputAddMemberPage


class AddMemberPage(BasePage):

	ele_add_member=(MobileBy.XPATH,"//*[@text='手动输入添加']")
	btn_back = (MobileBy.ID, 'com.tencent.wework:id/hbs')
	def go_to_manual_input_add_member(self):

		'''
		点击手动输入添加跳转到手动输入添加成员页面
		:return: 手动输入添加成员页面实例
		'''
		self.find(self.ele_add_member).click()
		return ManualInputAddMemberPage(self.driver)
		# return


	def go_to_contact(self):

		from test_app_work_wechat.po.contact_page import ContactPage
		'''
		点击返回，返回通信录页
		:return: 返回通讯录页面实例
		'''
		self.find(self.btn_back).click()
		return ContactPage(self.driver)
		# return



