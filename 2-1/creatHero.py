from ez import EZ
from hero import Hero
from jinx import Jinx
from police import Police
from timo import Timo


class CreatHero(Hero):
	def creatHero(self,name):
		if name == "ez":
			return
		if name == 'jinx':
			return Jinx()
		if name == 'police':
			return Police()
		if name == 'timo':
			return Timo()
		else:
			print('英雄不在英雄池中')
















