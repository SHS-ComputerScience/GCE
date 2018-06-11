import random

# Classes ------------------------------------------------------

class Player():
	def __init__(self):
		self.name = ""
		self.hp = 100
# 		self.shield = 100
		self.isDead = False

	def take_random_hit(self):
		self.hp -= random.randint(0, 50)
		if self.hp <= 0:
			self.isDead = True

	def display_stats(self):
		print(self.name, 'HP:', self.hp)

# -------------------------------------------------------------

n_players = 6
players = [Player() for x in range(n_players)]

players[0].name = 'Sadie'
players[1].name = 'Alfie'
players[2].name = 'Fola'
players[3].name = 'Connor'
players[4].name = 'Tom'
players[5].name = 'Max'

all_players_alive = True
while all_players_alive:
	for player in players:
		player.take_random_hit()
		player.display_stats()
		if player.isDead:
			all_players_alive = False
			print(player.name, 'is dead!')
			break

# deathlist.append(livinglist.pop(4))


