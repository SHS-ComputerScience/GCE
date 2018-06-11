#--------------------------------------------------------------------------------------------#
#------------------------------objective 6---------------------------------------------------#

# for counter in range(5):
# print("This is how you get code to repeat")

# for counter in range(7,12):
# print("The counter is",counter)

# word="Hello"
# for counter in range(0,len(word)):
# print("Letter",counter,"is",word[counter])

# for counter in range(10,0,-1):
# print(counter)

#-------------------------------------------------------------------------
# Squared challenge - 

# for counter in range(1,21):
#    squared = counter * counter
#    print(counter,"squared is",squared)


#--------------------------------------------------------------------------
# green bottles challenge -

# bottles = int(input("How many bottles are there sitting on the wall: "))
# for counter in range(bottles):
#    x = bottles - counter
#    print(x, "bottles sitting on the wall")


#---------------------------------------------------------------------------
# Times table challenge

##number = int(input("Enter a number between 1 and 12: "))
##
##for i in range(1, 13):
##    table = number * i
##    print(table)


#------------------------------------------------------------------------------
# Fibonacci sequence challenge

# n = ("Fibonacci Sequence")
# a = int(0)
# b = int(1)
# count = 0
# for i in range(20):
#    print(a)
#    new = a + b
#    a = b
#    b = new

#------------------------------------------------------------------------
# average calculator challenge 

# total = 0
# n = int(input("How many numbers would you like to be averaged? "))

# for i in range(n):
#     number = int(input("Enter number " + str(i + 1) + ": "))
#     total = total + number

# average = total / n
# print("The average is", average)

#------------------------------------------------------------------------
# FizzBuzz

# count = 0
# while (count < 101):
#    if (count % 5) == 0 and (count % 3) == 0:
#        print ("FizzBuzz")
#        count = count +1
#    elif (count % 3) == 0:
#        print ("Fizz")
#        count = count + 1
#    elif (count % 5) == 0:
#        print ("Buzz")
#        count = count +1
#    else:
#        print (count)
#        count = count + 1

#-------------------------------------------------------------------------
#times table challenge 2

# wrong = 0
# correct = 0

# question_1 = int(input("what is 2 * 2 ? "))
# if question_1 != 4:
# 	wrong = wrong + 1

# elif question_1 == 4:
# 	correct = correct + 1

# question_2 = int(input("what is 5 * 5 ? "))
# if question_2 != 25 :
# 	wrong = wrong + 1

# elif question_2 == 25:
#    	correct = correct + 1

# question_3 = int(input("what is 3 * 3 ? "))
# if question_3 != 9 :
# 	wrong = wrong + 1

# elif question_3 == 9:
#    	correct = correct + 1

# question_4 = int(input("what is 2 * 9 ? "))
# if question_4 != 18:
# 	wrong = wrong + 1

# elif question_4 == 18:
#    	correct = correct + 1

# question_5 = int(input("what is 4 * 2 ? "))
# if question_5 != 8:
# 	wrong = wrong + 1

# elif question_5 == 8:
#    	correct = correct + 1

# question_6 = int(input("what is 9 * 3 ? "))
# if question_6 != 27:
# 	wrong = wrong + 1

# elif question_6 == 27:
#    	correct = correct + 1

# question_7 = int(input("what is 10 * 3 ? "))
# if question_7 != 30:
# 	wrong = wrong + 1

# elif question_7 == 30:
#    	correct = correct + 1  
    
# question_8 = int(input("what is 1 * 1 ? "))
# if question_8 != 1:
# 	wrong = wrong + 1

# elif question_8 == 1:
#    	correct = correct + 1
    
# question_9 = int(input("what is 9 * 8 ? "))
# if question_9 != 72:
# 	wrong = wrong + 1

# elif question_9 == 72:
#    	correct = correct + 1   
    
# question_10 = int(input("what is 6 * 9 ? "))
# if question_10 != 54:
# 	wrong = wrong + 1

# elif question_10 == 54:
#    	correct = correct + 1   
    
# print("you got",correct,"questions correct ! ")
# print("you got",wrong,"questions wrong :(")

#------------------------------------------------------------------------
# ROT13

# import string
# word = input("Type a word to convert into ROT13: ")
# rot13 = str.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
# print(str.translate(word, rot13))















