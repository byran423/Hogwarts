from time import sleep

from selenium.webdriver.common.by import By

from base import Base


class TestWindows(Base):
	def test_window(self):
		self.driver.get('https://www.baidu.com/')
		# 点击登录
		ele_login = self.driver.find_element(By.XPATH,'//*[@id="s-top-loginbtn"]')
		ele_login.click()
		# 点击立即注册
		ele_sign=self.driver.find_element(By.XPATH,'//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a')
		ele_sign.click()
		self.driver.implicitly_wait(5)
		# 切换到新窗口
		windows = self.driver.window_handles
		self.driver.switch_to_window(windows[-1])
		# 输入手机号密码
		ele_name = self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__userName"]')
		ele_name.send_keys("nameyangbai")
		ele_phone = self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_4__phone"]')
		ele_phone.send_keys("18812341233")
		sleep(3)
		# 切换回原窗口，点击用户名登录
		self.driver.switch_to_window(windows[0])
		ele_user_login = self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__footerULoginBtn"]')
		ele_user_login.click()
		self.driver.implicitly_wait(5)
		self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys("yangbai423")
		self.driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys("123123")
		sleep(3)
		










