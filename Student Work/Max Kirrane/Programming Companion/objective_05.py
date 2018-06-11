#====================================================#
#                 OBJECTIVE 5                      #
#====================================================#

#----------------------------------------------------#
#                     TASKS                          #
#----------------------------------------------------#

#Gets user input

# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter a second number: "))

# #Make calculations
# power_of_result = number1 ** number2 
# division_result = number1 / number2 
# integer_division_result = number1 // number2
# modulus_result = number1 % number2

# #Output results
# print("")
# print(number1,"to the power of",number2,"is",power_of_result)
# print(number1,"divided by",number2,"is",division_result)
# print(number1,"divided by",number2,"is",integer_division_result)
# print(number1,"divided by",number2,"has a remainder of",modulus_result)

#----------------------------------------------------#
#                   CHALLENGES                       #
#----------------------------------------------------#

#-----------RPG dice challenge-----------#

# sides = int(input("Pick between a 4, 6 and a 12 sided dice: "))

# if sides == 4:
#     import random
#     random_number = random.randint(1,4)
#     print ("You rolled a ", random_number)
# elif sides == 6:
#     import random
#     random_number = random.randint(1,6)
#     print ("You rolled a ", random_number)
# elif sides == 12:
#     import random
#     random_number = random.randint(1,12)
#     print ("You rolled a ", random_number)


#-----------Divisible challenge-----------#

# n1 = int(input("Please enter a number: "))
# n2 = int(input("Please enter a bigger number: "))

# if n1 > n2 :
#     print("You can't beat me")

# number = (n2 /n1)

# intnumber = int(number)

# print ("Your first number goes into your second number",number,"times exactly, or",intnumber,"times")


#-----------Month challenge-----------#

# month = int(input("Enter a number between 1 and 12, according to the months of the year: "))

# if month == 1:
#     print("The month of January has 31 days")
# elif month == 2:
#     print("The month of February has 28 days, and 29 on a leapyear")
# elif month == 3:
#     print("The month of March has 31 days")
# elif month == 4:
#     print("The month of April has 30 days")
# elif month == 5:
#     print("The month of May has 31 days")
# elif month == 6:
#     print("The month of June has 30 days")
# elif month == 7:
#     print("The month of July has 31 days")
# elif month == 8:
#     print("The month of August has 31 days")
# elif month == 9:
#     print("The month of September has 30 days")
# elif month == 10:
#     print("The month of October has 31 days")
# elif month == 11:
#     print("The month of November has 30 days")
# elif month == 12:
#     print("The month of December has 31 days")


#-----------Dice game challenge-----------#

# import random
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# dice3 = random.randint(1,6)

# print ("The first dice rolled", dice1)
# print ("The second dice rolled", dice2)
# print ("The third dice rolled", dice3)

# if dice1 == dice2 == dice3:
#     print ("Your score is ",dice1 + dice2 + dice3)

# elif dice1 == dice3:
#     print ("Your score is ",dice1 + dice3 - dice2)

# elif dice2 == dice3:
#     print ("Your score is ",dice3 + dice2 - dice1)

# elif dice1 == dice2:
#     print ("Your score is ",dice1 + dice2 - dice3)

# elif dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
#     print ("Your score is 0")
