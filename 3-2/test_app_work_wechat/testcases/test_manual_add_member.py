from test_app_work_wechat.po.message_page import MessagePage


class TestManualAddMember():
	def test_manual_add_member(self):
		'''
		1、消息页面跳转到联系人页面
		2、联系人页面跳转到添加成员页面
		3、添加成员页面点击手动输入添加成员跳转到手动输入添加成员页面
		'''
		message_page =MessagePage()
		assert "测试" in message_page.go_to_contact().go_to_add_member().go_to_manual_input_add_member().manual_input_add_member().go_to_contact().get_member_list()










