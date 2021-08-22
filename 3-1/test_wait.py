from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.get('https://ceshiren.com/')
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def test_wait(self):
		self.driver.find_element(By.XPATH, '//*[@title="有新帖的话题"]').click()
		# def wait(x):
		# 	return len(self.driver.find_elements(By.XPATH,'//*[@class="views sortable num"]')) >= 1
		# expected_conditions.element_to_be_clickable()
		WebDriverWait(self.driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="views sortable num"]')))
		self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()
