from selenium import webdriver


class Base():

	def setup(self):
		option = webdriver.ChromeOptions()
		# 解决touchaction滑动操作时报错unknown command:Cannnot call non W3C standard command while in W3C mode，增加option.add_experimental_option('w3c',False)
		option.add_experimental_option('w3c', False)
		self.driver = webdriver.Chrome(options=option)

		self.driver.maximize_window()
		self.driver.implicitly_wait(5)

	def teardown(self):
		self.driver.quit()
