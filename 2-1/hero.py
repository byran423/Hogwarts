
class Hero():
	name = ''
	hp = 0
	power = 0

	def fight(self,enemy_name, enemy_hp, enemy_power):
		my_hp = self.hp - enemy_power
		enemy_final_hp = enemy_hp - self.power
		while True:
			my_hp -= enemy_power
			enemy_final_hp -= self.power

			if my_hp <=0 or enemy_final_hp<=0:
				if my_hp <= enemy_final_hp:

					print(enemy_name)
					return False
				if enemy_final_hp <= my_hp:
					print(f'{self.name}赢了')
					return False


	def speak_lines(self):
		if self.name == 'ez':
			print("是时候展现真正的技术了")
		if self.name == 'jinx':
			print('火力输出')
		if self.name == 'police':
			print('见识一下法律的子弹')
		if self.name == 'timo':
			print('timo队长正在待命')









