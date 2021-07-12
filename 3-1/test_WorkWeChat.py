import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base import Base


class TestWorkWeChat():
	def setup(self):
		# 设置复用浏览器
		# chrome_arg = webdriver.ChromeOptions()
		# chrome_arg.debugger_address = '127.0.0.1:9222'
		# self.driver = webdriver.Chrome(options=chrome_arg)

		# 不复用浏览器
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()




	def teardown(self):
		self.driver.quit()


	def test_WrokWeChatLogin(self):
		self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
		# 获取网站cookies
		# cookies = self.driver.get_cookies()
		# cookies = [{'domain': '.qq.com', 'expiry': 1622200962, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1622192912'}, {'domain': 'work.weixin.qq.com', 'expiry': 1622221453, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '95480pp'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850218088696'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5729978511'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1065967616'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325005460230'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'X0-qtd2ILFkiNa4xDdKEUXUxAVFaW88eCbotV_eiuQ6F6YQOuWj3snrpL7fwJeQs'}, {'domain': '.qq.com', 'expiry': 1622287302, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.644225127.1622157209'}, {'domain': '.work.weixin.qq.com', 'expiry': 1624792941, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1685272902, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1580255328.1622157209'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3625277029807634'}, {'domain': '.qq.com', 'expiry': 1855912786, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '3302812cdc80239c'}, {'domain': '.work.weixin.qq.com', 'expiry': 1653693207, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1426816'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwopen.open.sid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'wAC6XqetI1TM_O5Zqjq5ivqyMoQseyMhxqWd_eSiN0cZLg3dKoLJDfu8IeL_KXM1r'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s7368613991'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850218088696'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1928558951, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 7889545937, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%221706b2ae1eb229-06ea5af5085b5b-39697007-1296000-1706b2ae1ec9c3%22%2C%22%24device_id%22%3A%221706b2ae1eb229-06ea5af5085b5b-39697007-1296000-1706b2ae1ec9c3%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.nba01.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.nba01.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'vJQGu-rq2ytl6CothxlNUxMUSryJm_Oa7Z-05G5d6XqILyBrD63sjPusO0gFIMlY-0YiSFiqPID9sQb6TkWTXSkhXXUxan14d5VmrJhHI2KmLez6XZ4MIV-jTvxSAGbq2FCEfFeGcd5YS2O_hox73xhAhpgF6rN7O0BJHvR5e7KoWplBpg1Zc24Tlq9nNFZbyznJy6bk4K-QniV5xmRWlnTOrUDJeOp485nGrBTXr5Dy1TzKhRZsQwJypwNm0YjTB_qcZAarv3sBg3bgGD2cqg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1653728912, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1622157208,1622192912'}, {'domain': '.qq.com', 'expiry': 1856929458, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_547556017'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '547556017'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '734ea36d686fff258aa9481daabdeb9b16a45ae9c71c84d9a5185642f75d1d07'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False, 'value': 's1052378112'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'oso9m4mFFB'}]

		# print(cookies)

		# for cookie in cookies:
		# 	self.driver.add_cookie(cookie)

		# 重新打开带有cookie的页面
		# self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
		#
		#
		# assert "咩咩羊" == self.driver.find_element_by_class_name('index_info_name').text


		# 新建一个小数据库
		db = shelve.open('./mydbs/cookies')
		# # sleep(3)
		# # 把cookies内容放到cookies的db文件中
		# db['cookie'] = cookies
		# db.close()
		# 拿出cookies db数据
		cookies = db['cookie']
		for cookie in cookies:
			self.driver.add_cookie(cookie)

		self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')

		assert "咩咩羊" == self.driver.find_element_by_class_name('index_info_name').text










