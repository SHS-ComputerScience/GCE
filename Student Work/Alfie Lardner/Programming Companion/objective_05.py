#Objective 5



#-----------------------------------------------------------------------------------
#                                           TASKS
#-----------------------------------------------------------------------------------



##number1=int(input("Enter first number: "))
##number2=int(input("Enter second number: "))
##
##power_of_result = number1 ** number2
##division_result = number1 / number2
##integer_division_result = number1 // number2
##modulus_result = number1 % number2
##
##print()
##print(number1,"to the power of",number2,"is",power_of_result)
##print(number1,"divided by",number2,"is",division_result)
##print(number1,"divided by",number2,"is",integer_division_result)
##print(number1,"divided by",number2,"has a remainder of",modulus_result)




##import random
###Roll the dice
##random_number = random.randint(1,6)
##print("You rolled a",random_number)




##import random
###Roll the dice
##random_number = random.randint(1,10)
##print("You rolled a",random_number)



##import random
##
##dice = input("How many sides would you like on the dice (4, 6, 12): ")
##
##if dice == "4":
##    random_number = random.randint(1,4)
##    print("You rolled a",random_number)
##
##if dice == "6":
##    random_number2 = random.randint(1,6)
##    print("You rolled a",random_number2)
##
##if dice == "12":
##    random_number3 = random.randint(1,12)
##    print("You rolled a",random_number3)



#-----------------------------------------------------------------------------------
#                                RPG DICE CHALLENGE
#-----------------------------------------------------------------------------------


##import random
##
##dice = input("How many sides would you like on the dice (4, 6, 10, 12): ")
##
##if dice == "4":
##    random_number = random.randint(1,4)
##    print("You rolled a",random_number)
##
##if dice == "6":
##    random_number2 = random.randint(1,6)
##    print("You rolled a",random_number2)
##
##if dice == "10":
##    random_number3 = random.randint(1,10)
##    print("You rolled a",random_number3)
##
##if dice == "12":
##    random_number4 = random.randint(1,12)
##    print("You rolled a",random_number4)



#-----------------------------------------------------------------------------------
#                                DIVISIBLE CHALLENGE
#-----------------------------------------------------------------------------------


##number1 = int(input("Enter your first number: "))
##number2 = int(input("Enter your second number: "))
##
##divide = number1 // number2
##remainder = number1 % number2
##
##if number1 // number2:
##    print(number1 ,"is exactly divisible by", number2)
##
##if number1 % number2:
##    print(number1, "is not exactly divisible by", number2 ,"There is a remainder of" , remainder)



#-----------------------------------------------------------------------------------
#                                MONTH CHALLENGE
#-----------------------------------------------------------------------------------


##year = int(input("Enter the year: "))
##
##month = int(input("Enter a number between 1 and 12: "))
##
##if month == 1:
##    print("January has 31 days")
##
##if year % 4 and month  == 2:
##    print("February has 28 days because it is not a leap year")
##else:
##    print("February has 28 days because it is not a leap year")
##  
##
##if month == 3:
##    print("March has 31 days")
##
##if month == 4:
##    print("April has 30 days")
##
##if month == 5:
##    print("May has 31 days")
##
##if month == 6:
##    print("June has 30 days")
##
##if month == 7:
##    print("July has 31 days")
##
##if month == 8:
##    print("August has 31 days")
##
##if month == 9:
##    print("September has 30 days")
##
##if month == 10:
##    print("October has 31 days")
##
##if month == 11:
##    print("November has 30 days")
##
##if month == 12:
##    print("December has 31 days")


#-----------------------------------------------------------------------------------
#                                DICE GAME CHALLENGE   
#-----------------------------------------------------------------------------------

              
##import random
##
##dice1 = random.randint(1,6)
##print("The first number you rolled is a:",dice1)
##
##print("")
##
##dice2 = random.randint(1,6)
##print("The second number you rolled is a:",dice2)
##
##print("")
##
##dice3 = random.randint(1,6)
##print("The third number you rolled is a:",dice3)
##
##
##if dice1 == dice2 == dice3:
##    print("Your score is:",dice1 + dice2 + dice3)
##
##if dice1 == dice2:
##    print("Your score is:",(dice1 + dice2) - dice3)
##if dice1 == dice3:
##    print("Your score is:",(dice1 + dice3) - dice2)
##if dice2 == dice3:
##    print("Your score is:",(dice2 + dice3) - dice1)
##
##print("")
##
##if dice1 != dice2 and dice2 != dice3 and dice3 != dice1:
##    print("Your score is 0")
