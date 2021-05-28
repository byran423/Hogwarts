from time import sleep

import pytest

from base import Base


class TestJs(Base):
	@pytest.mark.skip
	def test_js_scroll(self):
		self.driver.get('https://www.baidu.com/')
		self.driver.find_element_by_id('kw').send_keys("selenium 测试")
		element = self.driver.execute_script("return document.getElementById('su')")
		element.click()
		sleep(3)
		self.driver.execute_script("document.documentElement.scrollTop=10000")
		self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
		sleep(3)
		print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

	def test_datetime(self):
		self.driver.get('https://www.12306.cn/index/')
		self.driver.execute_script("a=document.getElementById(id='train_date');a.removeAttribute('readonly');a.value='2020-12-12'")
		sleep(3)









