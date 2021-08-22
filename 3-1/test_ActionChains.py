from time import sleep, time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(5)
		self.driver.maximize_window()

	def teardown(self):
		self.driver.quit()

	def test_click(self):
		self.driver.get('http://sahitest.com/demo/clicks.htm')
		element_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
		element_double_click = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
		element_right_click = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
		action = ActionChains(self.driver)
		action.click(element_click)
		sleep(1)
		action.double_click(element_double_click)
		sleep(1)
		action.context_click(element_right_click)
		sleep(1)
		action.perform()
		sleep(3)

	def test_move(self):
		self.driver.get('http://www.baidu.com')
		ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
		action = ActionChains(self.driver)
		action.move_to_element(ele)
		action.perform()
		sleep(3)

	def test_dragdrop(self):
		self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
		drag_ele = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
		drop_ele = self.driver.find_element_by_xpath('/html/body/div[2]')

		action = ActionChains(self.driver)
		# action.drag_and_drop(drag_ele,drop_ele).perform()
		# action.click_and_hold(drag_ele).release(drop_ele).perform()
		action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
		sleep(3)

	def test_keys(self):
		self.driver.get('http://sahitest.com/demo/label.htm')
		ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
		ele.click()

		actions = ActionChains(self.driver)
		actions.send_keys("username").pause(1)
		actions.send_keys(Keys.SPACE).pause(1)
		actions.send_keys("tom")
		actions.send_keys(Keys.BACK_SPACE).pause(1).perform()
		sleep(3)
