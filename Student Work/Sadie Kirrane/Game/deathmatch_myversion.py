import random


# Classes -------------------


class Player():
	""" Player class """
	hp = 100
	is_dead = False

MIN_STRENGTH = 0
MAX_STRENGTH = 50

def __init__(self, name):
	""" Constructor """
	self.name = name

def attack(self, target):
	""" Player attack method """
	amount = random.randint(self.MIN_STRENGTH, self.MAX_STRENGTH)
	print(self.name, 'attacks', target.name, 'for', amount, 'hp!')
	target.defend(amount)

def defend(self, amount):
	""" Player defend method """
	self.hp -= amount
	if self.hp > 0:
		print(self.name, 'has', self.hp, 'hp remaining!\n')
	else:
		print(self.name, 'is dead!\n')
	self.is_dead = True


class Assassin(Player):
    """ Assassin player class """
    MIN_STRENGTH = 100
    MAX_STRENGTH = 100


class Tank(Player):
    """ Tank player class """
    hp = 200


class God(Player):
	""" This is a strict class that only Alfie can use """
	hp = 10000
	min_strength = 200
	max_strength = 200
# Functions -----------------

def get_random_player():
    """ Returns random player object from global players list """
    global players
    return random.choice(players)

def remove_from_list(player):
	global players
	index = players.index(player)
	players.pop(index)

# Main Program --------------

n_players = 8
players = God('Alfie'),
		Player('Arun'),
           Player('Charlie'),
           Player('Connor'),
           Assassin('Fola'),
           Tank('Max'),
           Player('Sadie'),
           Player('Tom')

last_player_standing = False

# Game Loop -----------------

while not last_player_standing:

	for player in players:
		target = get_random_player()
		player.attack(target)
	if target.is_dead:
		remove_from_list(target)
	if len(players) == 1:
		last_player_standing = True
#             all_players_alive = False
#             break
print(players[0].name, 'wins!!!')

print('Game Over!')
