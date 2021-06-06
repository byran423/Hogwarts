

class AddMemberPage():

	def add_member(self):
		'''
		添加成员操作
		:return:返回联系人页面实例
		'''
		# 导入操作放在方法内部解决循环导入的问题
		from test_work_wechat.po.contact_page import ContactPage

		return ContactPage()









