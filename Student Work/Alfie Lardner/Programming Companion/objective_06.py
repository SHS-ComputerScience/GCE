#-----------------------------------------------------------------------------------
#                                 TASKS
#-----------------------------------------------------------------------------------


##for counter in range(5):
##    print("This is how you get code to repeat")



##for counter in range(7,12):
##    print("The counter is",counter)



##word="Hello"
##for counter in range(0,len(word)):
##    print("Letter",counter,"is",word[counter])



#-----------------------------------------------------------------------------------
#                             SQUARE NUMBERS CHALLENGE
#-----------------------------------------------------------------------------------



# for counter in range(1, 21):
#    squared = counter * counter
#    print(counter,"squared is",squared)



#-----------------------------------------------------------------------------------
#                             9 GREEN BOTTLES CHALLENGE
#-----------------------------------------------------------------------------------
    


##bottles = int(input("How many bottles are there sitting on the wall: "))
##for counter in range(bottles):
##    y = bottles - counter
##    print(y, "bottles sitting on the wall")

# print("0 green bottles sitting on the wall")

#-----------------------------------------------------------------------------------
#                                 TIMES TABLE CHALLENGE 1
#-----------------------------------------------------------------------------------



##number = int(input("Enter a number between 1 and 12: "))
##
##for i in range(1, 13):
##    table = number * i
##    print(table)



#-----------------------------------------------------------------------------------
#                            FIBONACCI SEQUENCE CHALLENGE
#-----------------------------------------------------------------------------------



# def recur_fibo(n):
#   """Recursive function to
#   print Fibonacci sequence"""
#   if n <= 1:
#       return n
#   else:
#       return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 20


# nterms = int(input("How many terms? "))

# if nterms <= 0:
#   print("Plese enter a positive integer")
# else:
#   print("Fibonacci sequence:")
#   for i in range(nterms):
#       print(recur_fibo(i))




#-----------------------------------------------------------------------------------
#                             AVERAGE CALCULATOR CHALLENGE 
#-----------------------------------------------------------------------------------



     
#numbers = input("How many numbers you want to calculate? ")
#grade_list = []
#
#def evaluate():
#    for i in range (numbers):
#        grades = float(input("Please enter a number between 1-1000: "))
#        while grades < 0 or grades > 1000:
#            print ("The number " + str(grades) + " is out of range")
#            grades = float(input("Please enter a number between 1-1000: "))
#        grade_list.append(grades)
#    average = sum(grade_list)/numbers
#    print(average)
#try:
#    numbers = int(numbers)
#    evaluate()
#except:
#    while True:
#        try:
#            numbers = int(numbers)
#            evaluate()
#            break
#        except:
#            print("You should not enter " + str(numbers) + " because it is not an integer.")  
#            numbers = input("How many numbers you want to calculate? ")    





#-----------------------------------------------------------------------------------
#                                FIZZBUZZ CHALLENGE
#-----------------------------------------------------------------------------------



##count = 0
##while (count < 101):
##    if (count % 5) == 0 and (count % 3) == 0:
##        print ("FizzBuzz")
##        count = count +1
##    elif (count % 3) == 0:
##        print ("Fizz")
##        count = count + 1
##    elif (count % 5) == 0:
##        print ("Buzz")
##        count = count +1
##    else:
##        print (count)
##        count = count + 1



#-----------------------------------------------------------------------------------
#                              TIMES TABLE CHALLENGE 2
#-----------------------------------------------------------------------------------


##import random
##
##def questions():
##    name=input("What is your name: ")
##    print("Hello there",name,"!")
##
##    choice = random.choice("x")
##    finish = False
##    questionnumber = 0
##    correctquestions = 0
##
##    while finish == False:
##        if questionnumber < 10 | questionnumber >= 0:
##            number1 = random.randrange(1,10)
##            number2 = random.randrange(1,10)
##            print((number1),(choice),(number2))
##            answer=int(input("What is the answer?"))
##            questionnumber = questionnumber + 1
##
##            if choice==("+"):
##                realanswer = number1+number2
##                if answer==realanswer:
##                    print("That's the correct answer")
##                    correctquestions = correctquestions + 1
##                else:
##                    print("Wrong answer, the answer was",realanswer,"!")
##
##            if choice==("x"):
##                realanswer = number1*number2
##                if answer==realanswer:
##                    print("That's the correct answer")
##                    correctquestions = correctquestions + 1
##                else:
##                    print("Wrong answer, the answer was",realanswer,"!")
##
##            elif choice==("-"):
##                realanswer = number1-number2
##
##                if answer==realanswer:
##                    print("That's the correct answer")
##                    correctquestions = correctquestions + 1
##                else:
##                    print("Wrong answer, the answer was",realanswer,"!")
##        else:
##            finish = True
##    else:
##            print("Good job",name,"! You have finished the quiz")
##            print("You scored " + str(correctquestions) + "/10 questions.")
##
##questions()




#-----------------------------------------------------------------------------------
#                                   ROT13 CHALLENGE
#-----------------------------------------------------------------------------------



# import string
# word = input("Type a word to convert into ROT13: ")
# rot13 = str.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
# print(str.translate(word, rot13))




#-----------------------------------------------------------------------------------
#                                LETTER GAME CHALLENGE
#-----------------------------------------------------------------------------------



##scores = {'E' : 1,
##         'M' : 14,
##         'A' : 2,
##         'H' : 15,
##         'R' : 3,
##         'G' : 16,
##         'I' : 4,
##         'B' : 17,
##         'O' : 5,
##         'F' : 18,
##         'T' : 6,
##         'Y' : 19,
##         'N' : 7,
##         'W' : 20,
##         'S' : 8,
##         'K' : 21,
##         'L' : 9,
##         'V' : 22,
##         'C' : 10,
##         'X' : 23,
##         'U' : 11,
##         'Z' : 24,
##         'D' : 12,
##         'J' : 25,
##         'P' : 13,
##         'Q' : 26}
##
##score = 0
##users = input('Please enter your word: ')
##word = users.upper()
##
##for letter in word:
##   score = score + scores[letter]
##   
##print('The score of the word',users,'is',score)