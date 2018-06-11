###Objective 5
##
###Arithmetic Operations and Random Numbers
##
##dice = int(input("Choose between a 4, 6, or 12 sided dice")) 
##if dice == 4:
## import random
## random_number = random.randint(1,4)
## print("You rolled a",random_number)
##if dice == 6:
## import random
## random_number = random.randint(1,6)
## print("You rolled a",random_number)
##if dice == 12:
## import random
## random_number = random.randint(1,12)
## print("You rolled a",random_number)
##





##
###Divisible Challenge
##
##n1=int(input("Enter a number: "))
##n2=int(input("Enter a bigger number: "))
##
##if n1 == 0 :
## print("ERROR")
##
##if n2 == 0 :
## print("ERROR")
##
##
##print("The result of dividing your two numbers is",(n2/n1),".") 
##


###Month Challenge
##
##month = int(input("Enter a number between 1-12."))
##
##if month == 1:
## print ("Your chosen month is January. January has 31 days.")
## 
##if month == 2:
## print ("Your chosen month is February. February has 28 days usually, however in a leap year there is 29 days.")
##
##if month == 3:
## print ("Your chosen month is March. March has 31 days.")
## 
##if month == 4:
## print ("Your chosen month is April. April has 30 days.")
## 
##if month == 5:
## print ("Your chosen month is May. May has 31 days.")
## 
##if month == 6:
## print ("Your chosen month is June. June has 30 days.")
## 
##if month == 7:
## print ("Your chosen month is July. July has 31 days.")
## 
##if month == 8:
## print ("Your chosen month is August. August has 31 days.")
##
##if month == 9:
## print ("Your chosen month is September. September has 30 days.")
## 
##if month == 10:
## print ("Your chosen month is October. October has 31 days.")
## 
##if month == 11:
## print ("Your chosen month is November. November has 30 days.")
## 
##if month == 12:
## print ("Your chosen month is December. December has 31 days.") 


###Dice Game Challenge
##start = input("Press ENTER to roll three die")
##
##import random
##random_number1 = random.randint(1,6)
##
##import random
##random_number2 = random.randint(1,6)
##
##import random
##random_number3 = random.randint(1,6)
##
##
##print("You rolled",random_number1,random_number2,random_number3,".") 
##
##if (random_number1==random_number2==random_number3):
## total = random_number1 + random_number2 + random_number3
## print("Your score is",total,".") 
##
##
##if (random_number1==random_number2):
## total_1 = random_number1 + random_number2
## total_2 = total_1 - random_number3
## print("Your score is",total_2,".")
##
##if (random_number1==random_number3):
## total_3 = random_number1 + random_number3
## total_4 = total_3 - random_number2
## print("Your score is",total_4,".")
##
##if (random_number2==random_number3):
## total_5 = random_number2 + random_number3
## total_6 = total_5 - random_number1
## print("Your score is",total_6,".")
##
##if random_number1 != random_number2 != random_number3:
## print("Your score is 0.")
