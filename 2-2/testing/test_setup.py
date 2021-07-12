

def setup_module():
	print('模块级别的setup')

def teardown_module(self):
	print('模块级别的teardown')

def setup_function():
	print('函数级别的setup')
def teardown_function(self):
	print('函数级别的teardown')


def test_func1():
	print('测试函数1')

class TestDemo:

	def setup_class(self):
		print('类级别的 setup')

	def teardown_class(self):
		print('类级别的teardown')


	def setup(self):
		print('方法级别的setup')

	def teardown(self):
		print('方法级别的teardown')

	def test_demo1(self):
		print('test demo1')

	def test_demo2(self):
		print('test demo2')


class TestDemo2:

	def setup_class(self):
		print('类级别的 setup')

	def teardown_class(self):
		print('类级别的teardown')


	def setup(self):
		print('方法级别的setup')

	def teardown(self):
		print('方法级别的teardown')

	def test_demo1(self):
		print('test demo1')

	def test_demo2(self):
		print('test demo2')






