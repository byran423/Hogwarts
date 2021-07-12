from appium.webdriver.common.mobileby import MobileBy


from test_app_work_wechat.po.base_page import BasePage
from faker import Faker
fake = Faker('zh_CN')


class ManualInputAddMemberPage(BasePage):

	ele_name = (MobileBy.XPATH,"//*[contains(@resource-id,'com.tencent.wework:id/b09')]")
	ele_phone = (MobileBy.XPATH,"//*[contains(@resource-id,'com.tencent.wework:id/f7y')]")
	btn_save = (MobileBy.XPATH,"//*[contains(@resource-id,'com.tencent.wework:id/ad2')]")

	def manual_input_add_member(self):
		from test_app_work_wechat.po.add_member_page import AddMemberPage
		'''
		手动输入添加用户，并点击保存
		:return: 添加成员页实例
		'''

		self.find(self.ele_name).send_keys('测试')
		self.find(self.ele_phone).send_keys('13311112222')
		self.find(self.btn_save).click()







		return AddMemberPage(self.driver)
		# return










