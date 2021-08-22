from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_work_wechat.po.add_member_page import AddMemberPage
from test_work_wechat.po.base_page import BasePage
from test_work_wechat.po.contact_page import ContactPage


class MainPage(BasePage):
	_base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

	def goto_contact(self):
		'''
		跳转到通讯录页面
		:return:返回通讯录页面实例
		'''
		return ContactPage(self.driver)

	def goto_add_member(self):
		'''
		跳转到添加成员页面
		:return:返回添加联系人页面实例
		'''

		# 点击添加成员跳转到添加成员页
		self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
		return AddMemberPage(self.driver)







