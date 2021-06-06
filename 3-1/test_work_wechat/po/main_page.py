from selenium import webdriver

from test_work_wechat.po.add_member_page import AddMemberPage
from test_work_wechat.po.contact_page import ContactPage


class MainPage():
	def goto_contact(self):
		'''
		跳转到通讯录页面
		:return:返回通讯录页面实例
		'''
		return ContactPage()

	def goto_add_member(self):
		'''
		跳转到添加成员页面
		:return:返回添加联系人页面实例
		'''
		option = webdriver.ChromeOptions()
		option.add_experimental_option('w3c', False)
		self.driver = webdriver.Chrome(options=option)
		return AddMemberPage()







