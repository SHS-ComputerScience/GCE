#====================================================#
#                   OBJECTIVE 7                      #
#====================================================#

#     print ("3.Quit")

# no = int(input("Enter a number between 1 and 3, according to your choice: "))


#-----------Compound interest challenge-----------#

# balance = int(input("Enter your current balance in pounds: "))
# rate = float(input("Enter the interest rate (*.**):"))
# reach = int(input("Enter the desired balance that you want to reach: "))
# percent = (rate * 100)

# while reach > balance:
#     print ("£", balance,"starting balance-",percent, "% interest rate","(",rate,")")            
#     uno = ("Year 1: New balance=", balance, "+ (",balance,"*",rate,"=", balance * rate)
#     dos = ("Year 2: New balance=", uno, "+ (",uno,"*",rate,"=", uno * rate)
#     tres = ("Year 3: New balance=", dos, "+ (",dos,"*",rate,"=", dos * rate)       


#-----------Guess the number game challenge-----------#

# import random
# number = random.randint(1,100)

# tries = 1

# guess = int(input("Guess my number, between 1 and 100: "))

# while guess > number:
#     guess = int(input("Lower!: "))
#     tries = tries + 1

# while guess < number:
#     guess = int(input("Higher!: "))
#     tries = tries + 1

# else:
#     print ('Well done!')
#     print ('You guessed the number in',tries,'tries!')


#-----------Gamertag challenge-----------#

# Program that checks the length of gamertags entered

# valid_gamertag = True

# while valid_gamertag == True:
#     print ("Gamertags must not exceed 15 characters")
#     gamertag = input("Enter a gamertag: ")
#     gamertag_length = len(gamertag)

#     if gamertag_length > 15:
#         print ("Your gamertag is too long")
#     else:
#         print ("Gamertag accepted")
#         valid_gamertag = False


#-----------Rock, paper, scissors challenge-----------#

# print ("")
# print ("We are going to play a game of rock, paper, scissors")
# print ("The game is won once one player has beaten the other 10 times")
# print ("")
# choice = input("Pick rock, paper or scissors: ").lower()

# import random
# coPmp = random.choice(['rock', 'paper', 'scissors'])

# if choice == rock and comp == paper:
# 		print ("You picked rock")
# 		print ("Computer chooses paper")
# 		print ("Computer wins.")

# elif choice == rock and comp == scissors:
# 		print ("You picked rock")
# 		print ("Computer chooses scissors")
# 		print ("You win!")

# elif choice == rock and comp == rock:
# 		print ("You picked rock")
# 		print ("Computer chooses rock")
# 		choice = input("Go again; pick rock, paper or scissors: ").lower()

# elif choice == scissors and comp == paper:
# 		print ("You picked scissors")
# 		print ("Computer chooses paper")
# 		print ("You win!")

# elif choice == scissors and comp == scissors:
# 		print ("You picked scissors")
# 		print ("Computer chooses scissors")
# 		choice = input("Go again; pick rock, paper or scissors: ").lower()
	
# elif choice == paper and comp == paper:
# 		print ("You picked paper")
# 		print ("Computer choosses paper")
# 		choice = input("Go again; pick rock, paper or scissors: ").lower()


#-----------Happy numbers challenge-----------#

# def sum_of_squares(n):
# 	n_str = str(n)
# 	total = 0
# 	for i in range(len(n_str)):
# 		total += int(n_str[i]) ** 2
# 	return total

# def is_happy(n):
# 	repeat_list = []
# 	while True:
# 		n = sum_of_squares(n)
# 		if n == 1:
# 			return True
# 		else:
# 			if n in repeat_list:
# 				return False
# 			else:
# 				repeat_list.append(n)

# # main program
# number = int(input("Enter a positive number to check if it is happy or sad: "))

# if is_happy(number):
# 	print("This is one hella happy number! :)")
# else:
# 	print("This number may need a therapist! :(")


#--------------XP Challenge-------------------#

xp = 0
rank = 1

while rank < 5:
	game = int(input("Enter the amount of xp that you earned last game: "))
	total = (game + xp)
	if game >= 100 and rank == 1:
		print("You have been promoted to the rank of Corporal!")
		total_two = (total - 100)
		rank = (rank + 1) 
		print("Your total xp is", total_two)
	elif game >= 300 and rank == 2:
		print("You have been promoted to the rank of Sergeant!")
		total_two = (total - 300)
		rank = (rank + 1)
		print("Your total xp is", total_two)
	elif game >= 700 and rank == 3:
		print("You have been promoted to the rank of Staff Sergeant!")
		total_two = (total - 700)
		rank = (rank + 1)
		print("Your total xp is", total_two)
	elif game >= 1500 and rank == 4:
		print("You have been promoted to the rank of Warrant Officer!")
		total_two = (total - 1500)
		rank = (rank + 1)
		print("Your total xp is", total_two)
	else:
		print("You have not been promoted, try again")
		print("Your total xp is", total) 