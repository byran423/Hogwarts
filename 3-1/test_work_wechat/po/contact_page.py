from selenium.webdriver.common.by import By

from test_work_wechat.po.add_member_page import AddMemberPage
from test_work_wechat.po.base_page import BasePage


class ContactPage(BasePage):
	# 添加base_url可以支持测试用例灵活配置起始页
	# base_page完全和业务逻辑解耦
	_base_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

	def goto_add_meber(self):
		'''
		跳转到添加成员页面
		:return:返回添加成员页面实例
		'''
		return AddMemberPage(self.driver)

	def get_member_list(self):
		'''
		获取成员列表
		:return:返回用于断言的成员列表list
		'''
		el_name = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
		print(el_name)
		name_list = [i.text for i in el_name]
		print(name_list)
		return name_list
