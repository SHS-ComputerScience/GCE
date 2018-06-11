import random
# Classes ------------------------------------------------------

class Player():
	def __init__(self):
		self.name = ""
		self.hp = 100
		self.shield = 100
		self.isDead = False

	def checkIfDead(self):
		if self.hp <= 0:
			self.isDead = True

# -------------------------------------------------------------

n_players = 6
players = [Player() for x in range(n_players)]

players[0].name = 'Sadie'
players[1].name = 'Alfie'
players[2].name = 'Fola'
players[3].name = 'Connor'
players[4].name = 'Tom'
players[5].name = 'Max'

# for player in players:
# 	print(player.name)

all_players_alive = True
while all_players_alive:
	for i in range(len(players)):
		players[i].hp -= random.randint(0, 50) # random hit
		print(players[i].name, 'HP:', players[i].hp)
		players[i].checkIfDead()
		if players[i].isDead:
			all_players_alive = False
			print(players[i].name, 'is dead!')
			break