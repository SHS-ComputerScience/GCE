#--------------
#Objective 3
#--------------

#Task 1

#Working with strings
forename = input("Enter your surname: ")
forename_uppercase = forename.upper()
print("Your name is capital letter is:", forename_uppercase)

# Task 2
email = input("Enter your Email address: ")
email_lowercase = email.lower()
print("Your Email in lower case: ")

#Task 3
#Len returms the number of characters in a string
surname = input("Enter ur surname: ")
length_name = len(surname)
print("There are",lengeth_name,"letters in ur name.")

#Task 4
#[:?] returns a numbern of characters to the left of a string
sentence = "I saw a wolf in the forest. A lonely wolf."
character = sentence[:5]
print(characters)

#Task 5
sentence = "I saw a wolf in the forest. A lonely wolf."
character = sentence[-12:]
print(characters)

#Task 6
#[start:end] returns a number of characters in the middle of a string
sentence = "I saw a wolf in the forest. A lonely wolf."
characters = sentence[20:26]
print(characters)

#Task 7
#find returns the location of one string inside another
sentence = "I saw a wolf in the forest. A lonely wolf."
print(sentence)
word = input("Enter the word to find: ")
position = sentence.find(word)
print("The word",word,"is at character",position)

#Challenges

#Initials and surname challenge
forename = input("Enter your first name")
surname = input ("Enter your second name")

intial = forename[:]
