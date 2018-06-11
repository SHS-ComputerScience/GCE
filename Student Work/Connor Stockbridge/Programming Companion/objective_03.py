#                   Objective 3 - Connor Stockbridge - 12/09/2017

#                               Initials & Surname Chalenge
##Forename = str(input('What is your first name?'))
##Surname = str(input('What is your surname?'))
##Initial = Forename[:1]
##UpperIn = Initial.upper()
##UpperSur = Surname.upper()
##print(UpperIn,'.',UpperSur)

#                               Airline Ticket Challenge
##firstcity = input('What is your first destination?')
##secondcity = input('What is your second destination?')
##intOne = firstcity[:4].upper()
##intTwo = secondcity[:4].upper()
##print(intOne,'-',intTwo)

#                               Name Seperator Challenge
##full_name = str(input('Plese enter your full name:'))
##name_break = full_name.find(' ')
##first_name = full_name[0:name_break]
##last_name = full_name[name_break:]
##print('Forename:',first_name)
##print('Surname:',last_name)

#                               Word Extractor Challenge
#          ------------------------- Uncomplete-------------------------
##my_string = 'Quick brown fox jumps over the lazy dog.'
##print(my_string)
##users_word = input('What word do you choose?: ')
##first_index = my_string.find(users_word)
##start_point = first_index
##end_point = start_point + len(users_word)
##print(my_string[:start_point] + my_string[end_point:])
