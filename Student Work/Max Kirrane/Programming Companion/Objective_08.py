 #====================================================#
#                   OBJECTIVE 8                      #
#====================================================#

#----------------------------------------------------#
#                     TASKS                          #
#----------------------------------------------------#

# #Global variables accessed by all subroutines
# MaxNoOfStars=0
# NoOfStars=0
# NoOfSpaces=0

# #Set the size of the pyramid of stars
# def InitialiseNoOfSpacesAndStars():
# 	global NoOfSpaces, MaxNoOfStars, NoOfStars
# 	MaxNoOfStars=int(input("How many stars at the base (1-40)? "))
# 	#Calculate spaces needed from tip
# 	NoOfSpaces = MaxNoOfStars // 2
# 	#Set tip of pyramid to one star
# 	NoOfStars = 1

# #Outputs spaces before stars
# def OutputLeadingSpaces():
# 	global NoOfSpaces
# 	for count in range(NoOfSpaces):
# 			print(" ",end="")

# #Outputs stars
# def OutputLineOfStars():
# 	global NoOfStars
# 	for count in range(NoOfStars):
# 		print("*",end="")
# 	#Move to next line
# 	print()

# #Adjusts number of stars & spaces after output
# def AdjustNoOfSpacesAndStars():
# 	global NoOfSpaces, NoOfStars
# 	NoOfSpaces = NoOfSpaces - 1
# 	NoOfStars = NoOfStars + 2

# #Main program starts here
# InitialiseNoOfSpacesAndStars()
# while NoOfStars <= MaxNoOfStars:
# 	OutputLeadingSpaces()
# 	OutputLineOfStars()
# 	AdjustNoOfSpacesAndStars()

	
	
# #Program to output a set of random numbers
# import random
# #Output random numbers
# def outputrandoms(n,m):
# 	for counter in range(1,n+1):
# 		randomnum = random.randint(1,m)
# 		print("Number",counter,"is",randomnum,)

# #Main program starts here
# number=int(input("How many numbers do you want to output? "))
# maximum=int(input("What is the maximum number? "))
# outputrandoms(number, maximum)


# #How functions can be used
# #Returns a positive number from subtraction
# def floor(a, b):
# 	f = a - b
# 	if f > 0:
# 		return f
# 	else:
# 		return 0
	
# #Main program starts here
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# print("The floor number is:",floor(num1, num2))

#----------------------------------------------------#
#                   CHALLENGES                       #
#----------------------------------------------------#

#-----------VAT challenge-----------#

# #Returns VAT for the item
# price = int(input("Enter the price of an item you are going to buy in pounds:"))
# vat = (price * 1.2)
# vattwo = round(vat, 2)

# print ("The price of the item after VAT is £",vattwo)


#-----------Conversion challenge-----------#

#Converts from metric to imperial measurements

# print ("")
# print ("This calculator can convert metric measurements into imperial ones")
# print ("")
# print ("It can translate:")
# print ("-Centimetres into inches and feet")
# print ("-Metres into feet")
# print ("-Kilometres into miles")
# print ("-Kilograms into pounds")
# print ("-Litres into gallons")
# print ("")

# type = input("Which measurement of the above list do you want to convert: ").lower()

# if type == "centimetres":
# 	cm = int(input("How many centimetres do you want to convert into inches and feet: "))
# 	inch = (cm * 0.393701)
# 	foot = (inch / 12)
# 	inchy = round(inch,2)
# 	footy = round(foot,2)
# 	print (cm,"centimetres is", inchy,"inches and",footy,"feet")
	
# if type == "metres":
# 	metre = int(input("How many metres do you want to convert into feet: "))
# 	foot = (metre * 0.3048000097536)
# 	ametre = round(foot,2)
# 	print (metre,"metres is", ametre,"feet")
	
# if type == "kilometres":
# 	kilometres = int(input("How many kilometres do you want to convert into miles: "))
# 	mile = (kilometres * 0.621371)
# 	akilometre = round(mile,2)
# 	print (kilometres,"kilometres is", akilometre,"miles")
	
# if type == "kilograms":
# 	kilograms = int(input("How many kilograms do you want to convert into pounds: "))
# 	pound = (kilograms * 2.204620823516057)
# 	akilogram = round(pound,2)
# 	print (kilograms,"kilograms is", akilogram,"pounds")
	
# if type == "litres":
# 	litres = int(input("How many litres do you want to convert into gallons: "))
# 	gallon = (litres * 0.219969)
# 	alitre = round(gallon,2)
# 	print (litres,"litres is", alitre,"gallons")


#-----------Darts challenge-----------#

print ("Bitch we finna play some dartarinos")
score = 501
print("New game. Player starts at 501 points.")

while score != 0:
	total = int(input("Enter your total score from 3 darts: "))
	score = score - total
	if score < 0:
          score = score + total
          print('Unfortunate Score. Your score is still',score)
	elif score >= 1:
		print ("Your new score is", score)
	elif score == 0:
			print("Winner!")

			
#-----------Darts challenge part 2-----------#