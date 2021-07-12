from test_work_wechat.po.main_page import MainPage


class TestAddMember():
	def test_add_member(self):
		main_page = MainPage()
		# 1、跳转到add_member 页面
		# 2、做一个添加成员操作,点击保存跳转到通讯录页面
		# 3、在通讯录页面获取成员信息，作为断言
		assert "测试" in main_page.goto_add_member().add_member().get_member_list()











