from test_hero.ez import EZ
from test_hero.hero import Hero
from test_hero.jinx import Jinx
from test_hero.police import Police
from test_hero.timo import Timo


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
















