#Free for all Deathmatch

print("The match has begun")
print("")

import random
import time

# Classes -------------------

class Player():
	""" Player class """
	hp = 100
	is_dead = False
	
	damage = 0
	
	MIN_DAMAGE = 1
	MAX_DAMAGE = 50
	
	def __init__(self,name):
		""" Constructor """
		self.name = name
	
	def attack(self, target):
		
		""" Player attack method """
		if target == self:
			MIN_DAMAGE = 0
			MAX_DAMAGE = 0
		else:
			damage = random.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)
			if damage == target.hp:
				self.hp - damage
				print(self.name,'attacks', target.name, 'for', damage, 'hp!')
				print(target.name,' DEFLECTED', self.name, "'s attack and dealt", damage, 'damage!')
				
			else:
				print(self.name,'attacks', target.name, 'for', damage, 'hp!')
				target.defend(damage)
				
			print("")
			
	def defend(enemy,damage):
		""" Player defend method"""
		#All Players regenerate 20 health when damage is a prime number
		if damage >= 0:
		   # check for factors
		   for i in range(1,damage):
			   if (damage % i) == 0:
				   enemy.hp -= damage
				   if enemy.hp > 0:
					   print(enemy.name, 'has', enemy.hp, 'hp remaining!')
				   else:
					   print(enemy.name, 'is dead!')
					   enemy.is_dead = True
				   break
			   else:
				   print(enemy.name,"gets HEALTH BOOST")
				   print(enemy.name, 'had', enemy.hp, 'hp remaining')
				   enemy.hp += 20
				   print(enemy.name, 'now has', enemy.hp, 'hp remaining')
				   break

		print("")
		time.sleep(1)
		
		
class Beast(Player):
	MIN_DAMAGE = 0
	MAX_DAMAGE = 100
	hp = 200

# Functions -------------

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
players = [Beast('Rocky'),
		  Player('Iron Man'),
		  Player('Hulk'),
		  Player('Thor'),
		  Player('Captain America'),
		  Player('Thanos'),
		  Player('Black Widow'),
 		  Player('Black Panther')]
			
last_player_standing = False

#Game loop----------------

while not last_player_standing:

	for player in players:
		target = get_random_player()
		player.attack(target)
		if target.is_dead:
			remove_from_list(target)
		if len(players) == 1:
			last_player_standing = True

print(players[0].name, 'wins!!!')

print ('Victory Royale!')

# add critical hits
