


#------------------------------------------------
# Tasks
#------------------------------------------------

# #Global variables accessed by all subroutines
# MaxNoOfStars=0
# NoOfStars=0
# NoOfSpaces=0

# #Set the size of the pyramid of stars
# def InitialiseNoOfSpacesAndStars():
#     global NoOfSpaces, MaxNoOfStars, NoOfStars
#     MaxNoOfStars=int(input("How many stars at the base (1-40)? "))
#     #Calculate spaces needed from tip
#     NoOfSpaces = MaxNoOfStars // 2
#     #Set tip of pyramid to one star
#     NoOfStars = 1
    
# #Outputs spaces before stars
# def OutputLeadingSpaces():
#     global NoOfSpaces
#     for count in range(NoOfSpaces):
#         print(" ",end="")

# #Outputs stars
# def OutputLineOfStars():
#     global NoOfStars
#     for count in range(NoOfStars):
#         print("*",end="")
# #Move to next line
# print()

# #Adjusts number of stars & spaces after output
# def AdjustNoOfSpacesAndStars():
#     global NoOfSpaces, NoOfStars
#     NoOfSpaces = NoOfSpaces - 1
#     NoOfStars = NoOfStars + 2

# #Main program starts here
# InitialiseNoOfSpacesAndStars()
# while NoOfStars <= MaxNoOfStars:
#     OutputLeadingSpaces()
#     OutputLineOfStars()
#     AdjustNoOfSpacesAndStars()




# #Program to output a set of random numbers
# import random
# #Output random numbers
# def outputrandoms(n,m):
#     for counter in range(1,n+1):
#         randomnum = random.randint(1,m)
#         print("Number",counter,"is",randomnum)

#         #Main program starts here
# number=int(input("How many numbers do you want to output? "))
# maximum=int(input("What is the maximum number? "))
# outputrandoms(number, maximum)



# #How functions can be used
# #Returns a positive number from subtraction
# def floor(a, b):
#     f = a - b
#     if f > 0:
#         return f
#     else:
#         return 0
# #Main program starts here
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# print("The floor number is:",floor(num1, num2))





# -----------------------------------------------
#  VAT Challenge
# -----------------------------------------------
 

# def vat(a, b):
#     v = (a / b) + a
#     if a < 0:
#         print("No VAT added" , a)
#     else:
#         return v
    
# price = int(input("What is the price of the item: "))  
# vat1 = int(input("What is the VAT percentage: "))    
# print("The total price:",vat(price, vat1))  
      
    
    
# -----------------------------------------------
#  Conversion Challenge
# -----------------------------------------------
 
def mile(a):
    m = a * 0.62137
    if a > 0:
        return m
    else:
        return 0
    
def fahrenheit(c):
    f = (c * 1.8) + 32
    return f

def pound(e):
    p = e * 2.2046
    if e > 0:
        return p
    else:
        return 0
    
print("")
print("1. Kilometers to Miles")
print("2. Celcius to Fahrenheit") 
print("3. Kilograms to pounds")
print("")
option = int(input("Choose a conversion : "))

if option == 1:
    km = float(input("Enter length in kilometers: "))
    print(km, "kilometers in miles is:",mile(km))
    
if option == 2:
    ce = float(input("Enter temperature in celcius: "))
    print(ce, "celcius in fahrenheit is:",fahrenheit(ce))
    
if option == 3:
    kg = float(input("Enter weight in kilograms: "))
    print(kg, "kilograms in pounds is:",pound(kg))
    
    
    
# -----------------------------------------------
#  Conversion Challenge Part 2
# -----------------------------------------------
 
# def mile(a):
#     m = a * 0.62137
#     if a > 0:
#         return m
#     else:
#         return 0
    
# def fahrenheit(c):
#     f = (c * 1.8) + 32
#     return f

# def pound(e):
#     p = e * 2.2046
#     if e > 0:
#         return p
#     else:
#         return 0
   
#     print("")    
# measurement = input("Enter a metric measurement to convert it into imperial, for example: 25 kilograms: ")


    
    
# -----------------------------------------------
#  Darts Challenge 
# -----------------------------------------------



# start_score = 501
# print("")
# print("  _____             _        ")
# print(" |  __ \           | |       ")
# print(" | |  | | __ _ _ __| |_ ___  ")
# print(" | |  | |/ _` | '__| __/ __| ")
# print(" | |__| | (_| | |  | |_\__ \ ")
# print(" |_____/ \__,_|_|   \__|___/ ")
# print("")
# print("New Game! Player score = 501")

# while start_score > 0:
#     dartScore = int(input("Enter the total of your 3 darts: "))
#     start_score = start_score - dartScore
#     print("Your new score is:", start_score)
# if player_score == 0:
#     print("You have won!")




# -----------------------------------------------
#  Darts Challenge Part 2
# -----------------------------------------------
 
# player1 = 501
# player2 = 501
 
# print("  _____             _        ")
# print(" |  __ \           | |       ")
# print(" | |  | | __ _ _ __| |_ ___  ")
# print(" | |  | |/ _` | '__| __/ __| ")
# print(" | |__| | (_| | |  | |_\__ \ ")
# print(" |_____/ \__,_|_|   \__|___/ ")
# print("")
    
# print("New Game!")
# print("Player 1 score = 501 , player 2 score = 501")
# print("")

# while player1 > 0 and player2 > 0:
#     p1Score = int(input(" Player 1 - Enter score of your 3 darts (1 - 180)"))
#     player1 = player1 - p1Score
#     print("Your new score is:",player1)
#     p2Score = int(input("Player 2 - Enter score of your 3 darts (1 - 180) "))
#     player2 = player2 - p2Score
#     print("Your new score is:",player2)
    
# if player1 == 0:
#     print("Player 1 has won!")
# if player2 == 0:
#     print("Player 2 has won!")
    
    

# -----------------------------------------------
#  Snake Eyes Challenge 
# -----------------------------------------------
 
# import random    
    
# p1BankedTotal = 0
# p1RunningTotal = 0

# p2BankedTotal = 0
# p2RunningTotal = 0

# p1Dice1 = random.randint(1,6)
# p1Dice2 = random.randint(1,6)
# p1DieTotal = p1Dice1 + p1Dice2
# print("You rolled a", p1Dice1 , "and a", p1Dice2)

# p1RunningTotal = p1RunningTotal + p1DieTotal
# print("Your running total is:", p1RunningTotal)

# if p1Dice1 == 1 or p1Dice2 == 1:
# 	p1RunningTotal = 0
# 	print("You rolled a one, your running total has been reset to 0")
# if p1Dice1 == 1 and p1Dice2 == 1:
# 	p1BankedTotal = 0
# 	print("You rolled a double one, your banked total has been reset to 0")
	
# if p1Dice1 != 1 and p1Dice2 != 1:
# 	choice = input("Type bank to bank your points, or type gamble to gamble your points: ")

# 	if choice == "Bank" or choice == "bank":
# 		p1BankedTotal = p1BankedTotal + p1DieTotal
# 		p1RunningTotal = 0
# 		print("Running total has been reset, new banked total is:",p1BankedTotal)
# if choice == "Gamble" or "gamble":
# 	p1Dice1 = random.randint(1,6)
# 	p1Dice2 = random.randint(1,6)
# 	p1DieTotal = p1Dice1 + p1Dice2
# 	print("You rolled a", p1Dice1 , "and a", p1Dice2)

# 	p1RunningTotal = p1RunningTotal + p1DieTotal
# 	print("Your running total is:", p1RunningTotal)
	
# if p1Dice1 == 1 or p1Dice2 == 1:
# 	p1RunningTotal = 0
# 	print("You rolled a one, your running total has been reset to 0")
# if p1Dice1 == 1 and p1Dice2 == 1:
# 	p1BankedTotal = 0
# 	print("You rolled a double one, your banked total has been reset to 0")
	
# if p1Dice1 != 1 and p1Dice2 != 1:
# 	input("Type bank to bank your points, or type gamble to gamble your points: ")
	
# 	if choice == "Bank" or choice == "bank":
# 		p1BankedTotal = p1BankedTotal + p1DieTotal
# 		p1RunningTotal = 0
# 		print("Running total has been reset, new banked total is:",p1BankedTotal)

# 	if choice == "Gamble" or "gamble":
# 	p1Dice1 = random.randint(1,6)
# 	p1Dice2 = random.randint(1,6)
# 	p1DieTotal = p1Dice1 + p1Dice2
# 	print("You rolled a", p1Dice1 , "and a", p1Dice2)

# 	p1RunningTotal = p1RunningTotal + p1DieTotal
# 	print("Your running total is:", p1RunningTotal)
	

# if p1RunningTotal == 100:
# 	sys.exit()
		

