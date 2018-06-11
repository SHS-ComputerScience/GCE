# -----------------------------------------------
#  Menu selection challenge
# -----------------------------------------------

##menu = """1. Play Game
##2. Instructions
##3. Quit"""
##select = 1
##print(menu)
##while select > 0:
##    again = int(input("What do you want do?: "))
##    if again == 1:
##            print("Loading Game...")
##            break

# -----------------------------------------------
#  Compound interest challenge
# -----------------------------------------------

##print("Welcome to the Bank")
##balance = float(input("Enter current balance: £ "))
##dbalance = float(input("Enter desired balance: £ "))
##interestrate = float(input("Enter current interest rate as a decimal, e.g 0.04:"))
##count = 0
##while balance < dbalance:
##    count = count +1
##    interest = balance * interestrate
##    balance = balance  + interest
##    print(count, "£", balance)

# -----------------------------------------------
#  Guess the number game challenge
# -----------------------------------------------

#done on home file: SEND ASAP

# -----------------------------------------------
#  Gamertag challenge
# -----------------------------------------------

# gt = input("Enter wanted gamertag:  ")

# length = len(gt)

# select = 1

# while select > 0:
#     gt
#     if length <= 15:
#         print("Gamertag accepted!")
#         break
    
       
# -----------------------------------------------
#  Rock, paper, scissors challenge
# -----------------------------------------------

# import random

# a = input("Rock? Paper? Scissors?: ").lower()
# print("User:", a)

# list = ["rock","paper","scissors"]
# cpu = random.choice(list)
# print("CPU:", cpu)

# count = 0

# while not a == cpu:
#     count = count + 1
#     a = input("Rock? Paper? Scissors?: ").lower()
#     print("User:", a)
#     list = ["rock","paper","scissors"]
#     cpu = random.choice(list)
#     print("CPU:", cpu)

# -----------------------------------------------
#  Happy numbers challenge
# -----------------------------------------------



# -----------------------------------------------
#  XP Challenge
# -----------------------------------------------

# xp = 0
# rk = 0
# p = 0 
# c = 100
# sg = 300
# ss = 700
# wo = 1500

# while xp < 2000:
#     a = int(input("XP earned from the last game:"))
#     xp = a + xp
#     print("XP:", xp)
#     if xp >= c and xp <= sg:
#         print("Your a Corporal!")
#         xp = xp - c
#         print("New XP:", xp)
#     if xp >= sg and xp < ss:
#         print("Your a Sergeant!")
#         xp = xp - sg
#         print("New XP:", xp)
#     if xp >= ss and xp < wo:
#         print("Your a Staff Sergeant!")
#         xp = xp - sg
#         print("New XP:", xp)
#     if xp >= wo and xp < 2000:
#         print("Your a Warrant Officer!")
#         xp = xp - wo
#         print("New XP:", xp)
#     if xp >= 2000:
#         print("You completed the game. Congratulations")
#         break
        