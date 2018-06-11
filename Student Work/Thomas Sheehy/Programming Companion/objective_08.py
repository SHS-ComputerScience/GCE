# #Global variables accessed by all subroutines
# MaxNoOfStars=0
# NoOfStars=0
# NoOfSpaces=0
# #Set the size of the pyramid of stars
# def InitialiseNoOfSpacesAndStars():
# 	global NoOfSpaces, MaxNoOfStars, NoOfStars
# MaxNoOfStars=int(input("How many stars at the base (1-40)? "))
# #Calculate spaces needed from tip
# NoOfSpaces = MaxNoOfStars // 2
# #Set tip of pyramid to one star
# NoOfStars = 1
# #Outputs spaces before stars
# def OutputLeadingSpaces():
# 	global NoOfSpaces
# for count in range(NoOfSpaces):
# 	print(" ",end="")
# #Outputs stars
# def OutputLineOfStars():
# 	global NoOfStars
# for count in range(NoOfStars):
# 	print("*",end="")
# #Move to next line
# print()
# #Adjusts number of stars & spaces after output
# def AdjustNoOfSpacesAndStars():
# 	global NoOfSpaces, NoOfStars
# NoOfSpaces = NoOfSpaces - 1
# NoOfStars = NoOfStars + 2
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
# 	print("Number",counter,"is",randomnum)
# #Main program starts here
# number=int(input("How many numbers do you want to output? "))
# maximum=int(input("What is the maximum number? "))
# outputrandoms(number, maximum)

#How functions can be used
#Returns a positive number from subtraction
def floor(a, b):
	friend = a - b
	if friend > 0:
		return friend
	else:
		return 0
#Main program starts here
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The floor number is:",floor(num1, num2))