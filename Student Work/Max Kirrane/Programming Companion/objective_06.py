#====================================================#
#                  OBJECTIVE 6                       #
#====================================================#

#----------------------------------------------------#
#                     TASKS                          #
#----------------------------------------------------#

# for counter in range(5):
#  	print("This is how you get code to repeat")

#  for counter in range(7,12):
#  	print("The counter is",counter)

#  word = ("Hello")
#  for counter in range(0,len(word)):
#  	print("Letter",counter,"is",word[counter])

#----------------------------------------------------#
#                   CHALLENGES                       #
#----------------------------------------------------#

#-----------Square numbers challenge-----------#

# for counter in range(1,21):#
# 	counter = counter + 1
# 	square = (counter * counter)
# 	print (counter, "squared is", square)

#-----------9 green bottles challenge-----------#

# bottles = int(input("How many bottles are sitting on the wall between 0 and 100: "))

# for counter in range(bottles):
# 		y = bottles - counter
# 		print (y, "green bottles sitting on the wall")
# 		if y == 1:
# 			print(y, "green bottle sitting on the wall")

#-----------Times tables challenge 1-----------#

# number = int(input("Enter a number between 1 and 12: "))

# if number < 1 or number > 12:
# 	number = int(input("Enter a number between 1 and 12: "))


# for i in range(0,13):
# 	print (i,"x", number,"=",(i * number))


#----------Fibonacci Sequence Challenge----------#
# def recur_fibo(n):
#   """Recursive function to
#   print Fibonacci sequence"""
#   if n <= 1:
#       return n
#   else:
#       return(recur_fibo(n-1) + recur_fibo(n-2))
#       
#       
# start_number = int(input("Enter the start number here "))
# end_number = int(input("Enter the end number here "))

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)

# print map(fib, range(start_number, end_number))

#-----------Average calculator challenge-----------#

# amount = int(input("Enter how many numbers you want to be averaged: "))
# total = 0

# for i in range(0,amount):
# 	number = int(input("Please enter a number: "))
# 	total = total + number
	
# final = total / amount
# print ("The average of your numbers is", final)

#-----------FizzBuzz-----------#

# value = 0 
# for i in range(0,100):
# 	value = value + 1
	
# 	if value % 3 == 0 and value % 5 == 0:
# 		print("FizzBuzz")

# 	elif value % 3 == 0:
# 		print("Fizz")
		
# 	elif value % 5 == 0:
# 		print("Buzz")
		
# 	else:
# 		print (value)

#-----------Times tables challenge 2-----------#

# print ("We are going to solve some maths problems")

# import random
# total = 0
# 
# for i in range(10):
#    a = random.randint(1,12)
#    b = random.randint(1,12)
#    result = a * b

#    print(a, "x", b, "= ", end=" ")
#    answer = 
#    int(input())

#    if answer == result:
#        print("You got it right!")
#        total = total + 1

#    else:
#        print("You got it wrong!")

# print ("You scored", total,"out of 10!,", total * 10,"%!")

#-----------ROT13 challenge-----------#

#hi = input("Enter some plain text: ")
#cipher = ""
#
#for letter in hi:
#    ordinal_value = ord(letter)
#    shifted_value = ordinal_value + 13
#    shifted_char = chr (shifted_value)
#    cipher = cipher + shifted_char

#  cipher += ord(letter) + 13

#print(cipher)

#-----------Letter game challenge-----------#

# letters1 = "EARIOTNSLCUDP"
# letters2 = "MHGBFYWKVXZJQ"
# scoresHx = "123456789ABCD"
# score = 0

# word = input("Enter a word: ").upper()

# for letter in word:
#    #calc score
#    index = letters1.find(letter)
# if index == -1:
#         index = letters2.find(letter)
#         value = int(scoresHx[index], 16) + 13
# else:
#     value = int(scoresHx[index], 16)
#     score = score + value
		
# print(score, "points!")
