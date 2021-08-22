from hero import Hero
from timo import Timo


class Police(Hero):
	name = 'police'
	hp = 1800
	power = 195

def test_hero():
	police = Police()
	timo = Timo()

	timo.fight(police.name,police.hp,police.power)
	timo.speak_lines()
	police.speak_lines()




