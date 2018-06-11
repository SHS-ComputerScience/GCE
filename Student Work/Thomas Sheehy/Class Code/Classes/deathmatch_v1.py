import random

class Player():
	hp = 100
	is_dead = False

	MIN_STRENGTH = 0
	MAX_STRENGTH = 50

	def __init__(self, name):
		self.name = name
	
	def attack(self, target):
		amount = random.randint(self.MIN_STRENGTH, self.MAX_STRENGTH)
		print(self.name, 'attacks', target.name, 'for', amount, 'hp!')
		target.defend(amount)
	
	def defend(self, amount):
		self.hp -= amount
		if self.hp > 0:
			print(self.name, 'has', self.hp, 'hp remaining!')
		else:
			print(self.name, 'is dead')
			self.is_dead = True
		print()


def get_random_player():
	global players
	return random.choice(players)

def remove_from_list(player):
	global players
	index = players.index(player)

n_players = 8
players = [Player('Alfie'),
		   Player('Arun'),
		   Player('Tom'),
		   Player('Connor'),
		   Player('Fola'),
		   Player('X'),
		   Player('Y'),
		   Player('Charlie')]

min_two_players_alive = True

while min_two_players_alive:
	
	for player in players:
		target = get_random_player()
		player.attack(target)
		if target.is_dead:
			remove_from_list(target)
			#min_two_players_alive = False
			#break
			
			
print("Game Over!")