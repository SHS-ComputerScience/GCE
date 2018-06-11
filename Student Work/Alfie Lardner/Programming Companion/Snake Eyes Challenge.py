import random

p1BankedTotal = 0
p1RunningTotal = 0
p2BankedTotal = 0
p2RunningTotal = 0
p1Over = False
p2Over = False

def player1():
	global p1RunningTotal
	global p1BankedTotal
	global p1Over
	p1Die1 = random.randint(1,6)
	p1Die2 = random.randint(1,6)

	p1DieTotal = p1Die1 + p1Die2
	p1RunningTotal = p1RunningTotal + p1DieTotal

	if p1Die1 == 1 or p1Die2 == 1:
		p1RunningTotal = 0
		print("You rolled a 1, your running total has been reset back to 0")
		print("You ended that turn with a banked total of:",p1BankedTotal, "and a running total of:",p1RunningTotal)
		p1Over = True

		if p1Die1 == 1 and p1Die2 == 1:
			p1RunningTotal = 0
			p1BankedTotal = 0
			print("You rolled a double 1, you lose both your banked and running total")
			print("You ended that turn with a banked total of 0 and a running total of 0")
			p1Over = True
		if p1Die1 != 1 and p1Die2 != 1:
			print("Would you like to:")
			print("1. Gamble")
			print("2. Bank")
		choice = int(input("Enter the number of your option: "))

		if choice == 1:
			print("You have chosen to gamble")
			p1Die1 = random.randint(1,6)
			p1Die2 = random.randint(1,6)
			p1DieTotal = p1Die1 + p1Die2
			p1RunningTotal = p1RunningTotal + p1DieTotal
		if choice == 2:
			print("You have chosen to bank")
			p1BankedTotal = p1BankedTotal + p1RunningTotal
			p1RunningTotal = 0
			p1Over = True

def player2():
	global p2RunningTotal
	global p2BankedTotal
	global p2Over
	p2Die1 = random.randint(1,6)
	p2Die2 = random.randint(1,6)

	p2DieTotal = p2Die1 + p2Die2
	p2RunningTotal = p2RunningTotal + p2DieTotal

	if p2Die1 == 1 or p2Die2 == 1:
		p2RunningTotal = 0
		print("You have rolled a one, running total has been reset")
		print("You ended that turn with a banked score of: ",p2BankedTotal, "and a running score of: ", p2RunningTotal)
		p2Over = True
	elif p2Die1 == 1 and p2Die2 == 1:
		p2BankedTotal = 0
		p2RunningTotal = 0
		print("You rolled a double 1, both running and banked total haave been reset back to 0")
		print("You ended that turn with a banked total of 0 and a running total of 0")
	if p2Die1 != 1 and p2Die2 != 1:
		print("Would you like to:")
		print("1. Gamble")
		print("2. Bank")
	choice2 = int(input("Enter the number of your option: "))

	if choice2 == 1:
		print("You have chosen to gamble")
		p2Die1 = random.randint(1,6)
		p2Die2 = random.randint(1,6)
		p2DieTotal = p2Die1 + p2Die2
		p2RunningTotal = p2RunningTotal + p2DieTotal

	if choice2 == 2:
		print("You have chosen to bank")
		p2BankedTotal = p2BankedTotal + p2RunningTotal
		p2Over = True

while p1BankedTotal < 100 and p2BankedTotal < 100:
	move = random.randint(1,2)
	if move == 1 or p2Over == True:
		print('Player 1s turn')
		p2Over = False
		player1()
		if p1BankedTotal >= 100:
			print('PLAYER 1 WINS')
		if move == 2 or p1Over == True:
			print('Player 2s turn')
			p10ver = False
			player2()
		if p2BankedTotal >= 100:
			print('PLAYER 2 WINS')
