#                   Objective 5 - Connor Stockbridge - 03/10/2017
#------------------------------RPG Dice Challenge-------------------------------------------
## import random
##sided_dice = input('How many sides does your dice have?:')
##value = int(sided_dice)
##score = random.randint(1,value)
##print('You rolled a',score)
#------------------------------Divisible Challenge-------------------------------------------
##first_value = int(input('What is your first number?:'))
##second_value = int(input('What is your second number?:'))
##product = first_value / second_value
##modulusresult = first_value % second_value
##if modulusresult != 0 :
##    print(first_value,'is not directley divisible by',second_value,',as there is a remanider of',modulusresult)
##else:
##    print(product)
##    print(first_value,'is directley divisible by',second_value)
#-----------------------------Month Challenge-------------------------------------------
##user_input = int(input('Pick a number from 1 to 12:'))
##year = int(input('What year is it?:'))
##modulus_result = year % 4
##
##if user_input == 1:
##    print('It is January and there is 31 days.')
##
##if user_input == 2:
##    if modulus_result != 0 :
##        print('It is Feburary and there is 28 days.')
##    else:
##        print('It is Feburary and there is 29 days.')
##                 
##if user_input == 3:
##    print('It is March and there is 31 days.')
##
##if user_input == 4:
##    print('It is April and there is 30 days.')
##
##if user_input == 5:
##    print('It is May and there is 31 days.')
##
##if user_input == 6:
##    print('It is June and there is 30 days.')
##
##if user_input == 7:
##    print('It is July and there is 31 days.')
##
##if user_input == 8:
##    print('It is August and there is 31 days.')
##
##if user_input == 9:
##    print('It is September and there is 30 days.')
##
##if user_input == 10:
##    print('It is October and there is 31 days.')
##
##if user_input == 11:
##    print('It is November and there is 30 days.')
##
##if user_input == 12:
##    print('It is December and there is 31 days.')
#-----------------------------------Dice Game Challenge-------------------------------------
########import random
########random.randint(1,6)
########matching =  {dice_1 == dice_2:r1, dice_1 == dice_3:r2, dice_3 == dice_2:r3}
########print(matching)
########    if dice_1 == dice_2 or dice_1 == dice_3 or dice_2 == dice_3:


##dice_1 = int(input('What was the first roll?:'))
##dice_2 = int(input('What was the second roll?:'))
##dice_3 = int(input('What was the third roll?:'))
##
##r1 = dice_1 == dice_2
##r2 = dice_1 == dice_3
##r3 = dice_3 == dice_2
##
##if dice_1 == dice_2 == dice_3:
##    score = dice_1 + dice_2 + dice_3
##    print('The score is',score)
##
##if dice_1 != dice_2 or dice_1 != dice_3 or dice_2 != dice_3:
##   if r1 is True:
##       score = dice_1 + dice_2
##       final_score = score - dice_3
##       print('The score is',final_score)
##       
##   elif r2 is True:
##       score = dice_1 + dice_3
##       final_score = score - dice_2
##       print('The score is',final_score)
##
##   elif r3 is True:
##       score = dice_3 + dice_2
##       final_score = score - dice_1
##       print('The score is',final_score)
##
##else:
##    score = 0
##    print('The score is',score)
