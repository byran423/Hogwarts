from time import sleep

from selenium.webdriver.common.by import By

from test_work_wechat.po.base_page import BasePage


class AddMemberPage(BasePage):
	_ele_username = (By.ID, 'username')
	_ele_memberAdd_english_name = (By.ID, 'memberAdd_english_name')
	_ele_memberAdd_acctid = (By.ID, 'memberAdd_acctid')
	_ele_memberAdd_phone = (By.ID, 'memberAdd_phone')

	def add_member(self):
		'''
		添加成员操作
		:return:返回联系人页面实例
		'''
		# 导入操作放在方法内部解决循环导入的问题
		from test_work_wechat.po.contact_page import ContactPage

		# 填写测试数据
		# *self.ele_username 解包元素参数，传入by,value两个参数
		# 在base_page里封装find方法后不需要手动解包
		self.find(self.ele_username).send_keys("测试")
		self.find(self.ele_memberAdd_english_name).send_keys("TEST")
		self.find(self.ele_memberAdd_acctid).send_keys("test0001")
		self.find(self.ele_memberAdd_phone).send_keys("13312331233")
		# 点击保存
		self.find(By.CSS_SELECTOR, ".js_btn_save").click()


		return ContactPage(self.driver)


	def add_member_failed(self):
		self.find(self.ele_username).send_keys("测试")
		self.find(By.ID, 'memberAdd_english_name').send_keys("TEST")
		self.find(By.ID, 'memberAdd_acctid').send_keys("test0001")
		self.find(By.ID, 'memberAdd_phone').send_keys("13312331233")









