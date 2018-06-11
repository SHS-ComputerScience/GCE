###Understanding string manipulation functions
##
##forename=input("Enter your surname: ")
##forename_uppercase=forename.upper()
##print("Your name in capital letters is:",forename_uppercase)
##
##
##email=input("Enter your email address: ")
##email_lowercase=email.lower()
##print("Your email address in lowercase is:",email_lowercase) 
##

##
###Len returns the number of characters in a string
##surname = input("Enter your surname: ")
##length_name = len(surname)
##print("There are",length_name,"letters in your name.")
##


###[:?] returns a number of characters to the left of a string
##sentence = "I saw a wolf in the forest. A lonely wolf."
##characters = sentence[:5]
##print(characters)


###[:?] returns a number of characters to the left of a string
##sentence = "I saw a wolf in the forest. A lonely wolf."
##characters = sentence[-12:]
##print(characters)



###[start:end] returns a number of characters in the middle of a string
##sentence = "I saw a wolf in the forest. A lonely wolf."
##characters = sentence[20:26]
##print(characters)

##
###find returns the location of one string inside another
##sentence = "I saw a wolf in the forest. A lonely wolf."
##print(sentence)
##word = input("Enter the word to find: ")
##position = sentence.find(word)
##print("The word",word,"is at character",position)
##
##
##
##name = input("Enter your name : ")
##age = int(input("Enter your age :"))
##new_age = age + 8
##print ("Thank you",name,". In 2025 you will be",new_age,".")
## 


###Initials and surname challenge
##forename = input("What is your forename? ")
##surname = input("What is your surname? ") 
##initial = forename[:1] 
##upper_initial = initial.upper()
##upper_surname = surname.upper() 
##print("Thank you",upper_initial,upper_surname,".")


###Airline ticket challenge
##city_one = input("Please list a city. ")
##city_two = input("Please list another city. ")
##city_1 = city_one[:4]
##city_2 = city_two[:4]
##c1 = city_1.upper()
##c2 = city_2.upper()
##print(c1,"-",c2)



###Name separator challenge
##name = input("Please enter your full name. ")
##full_name = name.split()
##print (full_name)


## Word Extractor challenge
##print("The quick brown fox jumps over the lazy dog")
##sentence = "The quick brown fox jumps over the lazy dog"
##word = input("Enter word to remove: ")
##
##first_index = sentence.find(word)
##last_index = first_index + " "
