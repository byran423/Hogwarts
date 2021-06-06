from test_work_wechat.po.add_member_page import AddMemberPage


class ContactPage():
	def goto_add_meber(self):
		'''
		跳转到添加成员页面
		:return:返回添加成员页面实例
		'''
		return AddMemberPage()


	def get_member_list(self):
		'''
		获取成员列表
		:return:返回用于断言的成员列表list
		'''
		return []









