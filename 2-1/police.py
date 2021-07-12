from test_hero.hero import Hero
from test_hero.timo import Timo


class Police(Hero):
	name = 'police'
	hp = 1800
	power = 195


police = Police()
timo = Timo()

timo.fight(police.name,police.hp,police.power)
timo.speak_lines()
police.speak_lines()




