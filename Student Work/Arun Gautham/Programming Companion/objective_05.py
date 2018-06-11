 
#RPG dice challenge

import random

diceSides = input('How many sides does your dice have?:')
value = int(diceSides)
score = random.randint(1,value)
print('You rolled a',score)

#Divisible challenge

value1 = int(input('What is your first number?:'))
value2 = int(input('What is your second number?:'))

product = value1 / value2
modulusresult = value1 % value2

if modulusresult != 0 :
    print(value1,'is not directley divisible by',value2,',as there is a remanider of',modulusresult)
else:
    print(product)
    print(value1,'is directley divisible by',value2)
    
#Month challenge

userInput = int(input('Pick a number from 1 to 12:'))
year = int(input('What year is it?:'))
modResult = year % 4

if userInput == 1:
    print('It is January and there is 31 days.')

if userInput == 2:
    if modResult != 0 :
        print('It is Feburary and there is 28 days.')
    else:
        print('It is Feburary and there is 29 days.')
                 
if userInput == 3:
    print('It is March and there is 31 days.')
if userInput == 4:
    print('It is April and there is 30 days.')
if userInput == 5:
    print('It is May and there is 31 days.')
if userInput == 6:
    print('It is June and there is 30 days.")
if userInput == 7:
    print('It is July and there is 31 days.')
if userInput == 8:
    print('It is August and there is 31 days.')
if userInput == 9:
    print('It is September and there is 30 days.')
if userInput == 10:
    print('It is October and there is 31 days.')
if userInput == 11:
    print('It is November and there is 30 days.')
if userInput == 12:
    print('It is December and there is 31 days.')
          
#Dice game challenge

import random
          
random.randint(1,6)
matching = {dice1 == dice2:r1, dice1 == dice3:r2, dice3 == dice2:r3}
print(matching)
    if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:


dice1 = int(input('What was the first roll?:'))
dice2 = int(input('What was the second roll?:'))
dice3 = int(input('What was the third roll?:'))

r1 = dice1 == dice2
r2 = dice1 == dice3
r3 = dice3 == dice2

if dice1 == dice2 == dice3:
    score = dice1 + dice2 + dice3
    print('The score is',score)

if dice1 != dice2 or dice1 != dice3 or dice2 != dice3:
   if r1 is True:
       score = dice1 + dice2
       finalScore = score - dice3
       print('The score is',finalScore)
       
   elif r2 is True:
       score = dice1 + dice3
       finalScore = score - dice2
       print('The score is',finalScore)

   elif r3 is True:
       score = dice3 + dice2
       finalScore = score - dice1
       print('The score is',finalScore)

else:
    score = 0
    print('The score is',score)
          
