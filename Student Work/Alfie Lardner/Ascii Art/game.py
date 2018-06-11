
import random

#Classes-------------

class Player():
	""" Player class """
	hp = 100
	is_dead = False

	min_strength = 0
	max_strength = 50

	def __init__(self, name):
		""" Constructor """
		self.name = name

	def attack(self, player):
		""" Player attack method """
		amount = random.randint(self.min_strength, self.max_strength)
		print(self.name, 'attacks', player.name, 'for', amount, 'hp!')
		player.defend(amount)

	def defend(self, amount):
		""" Player defend method """
		self.hp -= amount
		if self.hp > 0:
			print(self.name, 'has', self.hp, 'hp remaining!')
		else:
			print(self.name, 'is dead')
			self.is_dead = True
		print()




#Functions-------------

def get_random_player():
    """ Returns random player object from global players list """
    global players
    return random.choice(players)


#Main Program ------------

n_players = 8
players = [Player('Alfie'),
           Player('Arun'),
           Player('Charlie'),
           Player('Connor'),
           Player('Fola'),
           Player('Max'),
           Player('Sadie'),
           Player('Tom')]

last_player_standing = False

#Game Loop --------------

while not last_player_standing:

    for player in players:
        target = get_random_player()
        player.attack(target)
        if target.is_dead:

            all_players_alive = False
            break

            print('Game Over!')
