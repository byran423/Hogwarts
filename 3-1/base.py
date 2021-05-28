from selenium import webdriver


class Base():

	def setup(self):
		option = webdriver.ChromeOptions()
		option.add_experimental_option('w3c',False)
		self.driver = webdriver.Chrome(options=option)

		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
	def teardown(self):
		self.driver.quit()








