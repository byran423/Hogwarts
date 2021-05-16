#coding=utf-8
import yaml
from python_code.calc import Calculator
import pytest



class TestCalc:

	def setup_class(self):
		self.calc = Calculator()

	def setup(self):
		print('计算开始')

	def teardown(self):
		print('计算结束')

	# 读取calc.yaml文件
	with open('../datas/calc.yaml') as f:
		datas = yaml.safe_load(f)['add']
		add_datas = datas['datas']
		ids = datas['ids']
	with open('../datas/calc.yaml') as f:
		div_datas = yaml.safe_load(f)['div']
		div_data = div_datas['div_datas']
		div_ids = div_datas['div_ids']

	@pytest.mark.parametrize(
		"c,d,expect",
		div_data, ids=div_ids
	)
	def test_div(self, c, d, expect):
		result = self.calc.div(c,d)
		assert result == expect

	@pytest.mark.parametrize(
		"a,b,expect",
		add_datas,ids=ids
	)
	def test_add(self,a,b,expect):
		# 实例化计算器类
		# calc = Calculator()
		result = self.calc.add(a,b)
		assert round(result,2) == expect





























