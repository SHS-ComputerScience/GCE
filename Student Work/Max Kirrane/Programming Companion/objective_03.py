#==========================================================#
#                       OBJECTIVE 3                        #
#==========================================================#

#----------------------------------------------------------#
#                       TASKS                              #
#----------------------------------------------------------#

###name_enter = input("Enter your name:")
##
##enter_age = int(input("Enter your age:"))
##
##new_age = enter_age + 8
##
##print(name_enter, ", your age will be ", new_age, " by 2025")

                    
#-----------Working with strings-----------#

# surname = input("Enter your surname: ")
# length_surname = len(surname)

# print ("There are", length_surname, "letters in your surname")

# sentence = "Leo Messi is the best player in the world"
# print (sentence)

# word = input("Enter the word to find: ")
# position = sentence.find(word)
# print ("The word",word,"is at character",position)


##forename = input("Input Forename:")
##surname = input("Input Surname:")
##
##initial = forename[:1]
##upperinitial = initial.upper()
##uppersurname = surname.upper()
##
##print ("Your name is", upperinitial, ".", uppersurname)


#---------------------------------------------------------#
#                       CHALLENGES                        #
#---------------------------------------------------------#

#Initials & surname challenge

# forename = input("Enter your forename: ")
# surname = input("Enter your surname: ")

# initial = forename[:1]

# upperinitial = initial.upper()

# uppersurname = surname.upper()

# print (upperinitial,uppersurname)


#-----------Airline ticket challenge-----------#

# city_1 = input("Enter the name of a city: ")
# city_2 = input("Enter the name of another city: ")

# initial_1 = city_1.upper()[0:4]
# initial_2= city_2.upper()[0:4]

# print ("Your flight is", initial_1, "-", initial_2)



#-----------Name separator challenge-----------#

#Seperates the forename of the user from the surname

# fullname = str(input("Enter your forename, followed by your surname on this line: "))
# break1 = fullname.find(" ")
               
# firstname = fullname[0:break1]
# surname = fullname[break1 + 1:]

# foreinitial = firstname[0]
# surinitial = surname[0]

# upperfore = foreinitial.upper()
# uppersur = surinitial.upper()

# firt = firstname[1:]
# surt = surname[1:]

# print ("Forename:",upperfore + firt)
# print ("Surname:",uppersur + surt)


#-----------Word extractor challenge-----------#

# sentence = "Quick brown fox jumps over the lazy dog"

# print (sentence)

# word = str(input("Choose a word to remove from this sentence: "))

# sentence = sentence.replace(word,"")

# print (sentence)
