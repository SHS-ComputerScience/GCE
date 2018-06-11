#                   Objective 6 - Connor Stockbridge - 09/10/2017
#------------------------------Square Numbers Challenge-------------------------------------------
##for counter in range(0,20):
##    counter = counter + 1
##    squared = counter * counter
##    print(counter,'squared is',squared)
##    
#------------------------------9 green bottles Challenge-------------------------------------------    
##users_input = int(input('How many bottles are on the wall?:'))
##print(users_input,'green bottles sitting on the wall')
##
##for counter in range(0,users_input):
##    users_input = users_input - 1
##    print(users_input,'green bottles sitting on the wall')
#------------------------------Times Table Challenge 1-------------------------------------------
##users_input = int(input('Enter a number between 1 & 12:'))
##print('The',users_input,'Times Table.')
##
##for counter in range(0,12):
##    counter = counter + 1
##    result = users_input * counter
##    print(users_input,'multiplied by',counter,'is',result)
#------------------------------Fibonacci sequence challenge-------------------------------------------
##def recur_fibo(n):
##   """Recursive function to
##   print Fibonacci sequence"""
##   if n <= 1:
##       return n
##   else:
##       return(recur_fibo(n-1) + recur_fibo(n-2))
##
##nterms = 20
##
##
##nterms = int(input("How many terms? "))
##
##if nterms <= 0:
##   print("Plese enter a positive integer")
##else:
##   print("Fibonacci sequence:")
##   for i in range(nterms):
##       print(recur_fibo(i))
#------------------------------Average calculator challenge-------------------------------------------
##count = int(input('How may numbers are you going to enter:'))
##total = 0
##
##for i in range(0,count):
##   number = int(input('Please enter your first number:'))
##   total = total + number
##
##final = total / count
##print('The average of your numbers is',final)
#---------------------------------------FizzBuzz-----------------------------------------------
##value = 0
##for i in range(0,100):
##    value = value + 1
##
##    if value % 3 == 0 and value % 5 == 0:
##        print('FizzBuzz')
##        
##    elif value % 3 == 0:
##        print('Fizz')
##            
##    elif value % 5 == 0:
##        print('Buzz')
##
##    else:
##        print(value)
#---------------------------------------Times table challenge 2-----------------------------------------------
##import random
##
##for i in range(0,10):
##    value_1 = random.randint(1,10)
##    value_2 = random.randint(1,10)
##    print('What is',value_1,'multiplied by',value_2,'?')
##    user = int(input('What is your answer:'))
##    answer = value_1 * value_2
##
##    if answer == user:
##        print('Well Done!')
##
##    else:
##        print('Try Again....')
#---------------------------------------ROT13-----------------------------------------------
##import string
##word = input("Type a word to convert to ROT13: ")
##rot13 = str.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
##print(str.translate(word, rot13))
#---------------------------------------Letter game challenge-----------------------------------------------
##scores = {'E' : 1,
##          'M' : 14,
##          'A' : 2,
##          'H' : 15,
##          'R' : 3,
##          'G' : 16,
##          'I' : 4,
##          'B' : 17,
##          'O' : 5,
##          'F' : 18,
##          'T' : 6,
##          'Y' : 19,
##          'N' : 7,
##          'W' : 20,
##          'S' : 8,
##          'K' : 21,
##          'L' : 9,
##          'V' : 22,
##          'C' : 10,
##          'X' : 23,
##          'U' : 11,
##          'Z' : 24,
##          'D' : 12,
##          'J' : 25,
##          'P' : 13,
##          'Q' : 26}
##         
##score = 0
##users = input('Please enter your word: ')
##word = users.upper()
##
##for letter in word:
##    score = score + scores[letter]
##    
##print('The score of the word',users,'is',score)