#--------------------------------------------------------
#  Objective 8 
#--------------------------------------------------------

# #Global variables accessed by all subroutines
# MaxNoOfStars=0
# NoOfStars=0
# NoOfSpaces=0

# #Set the size of the pyramid of stars
# def InitialiseNoOfSpacesAndStars():
#     global NoOfSpaces, MaxNoOfStars, NoOfStars
#     MaxNoOfStars=int(input("How many stars at the base (1-40)? "))
#     #Calculate spaces needed from tip
#     NoOfSpaces = MaxNoOfStars // 2
#     #Set tip of pyramid to one star
#     NoOfStars = 1
    
# #Outputs spaces before stars
# def OutputLeadingSpaces():
#     global NoOfSpaces
#     for count in range(NoOfSpaces):
#         print(" ",end="")
        
# #Outputs stars
# def OutputLineOfStars():
#     global NoOfStars
#     for count in range(NoOfStars):
#         print("*",end="")
#     #Move to next line
#     print()
    
# #Adjusts number of stars & spaces after output
# def AdjustNoOfSpacesAndStars():
#     global NoOfSpaces, NoOfStars
#     NoOfSpaces = NoOfSpaces - 1
#     NoOfStars = NoOfStars + 2

# #Main program starts here
# InitialiseNoOfSpacesAndStars()
# while NoOfStars <= MaxNoOfStars:
#     OutputLeadingSpaces()
#     OutputLineOfStars()
#     AdjustNoOfSpacesAndStars()


# #Program to output a set of random numbers
# import random
# #Output random numbers
# def outputrandoms(n,m):
#     for counter in range(1,n+1):
#         randomnum = random.randint(1,m)
#         print("Number",counter,"is",randomnum)


# #Main program starts here
# number=int(input("How many numbers do you want to output? "))
# maximum=int(input("What is the maximum number? "))
# outputrandoms(number, maximum)

#------------------------------------------------------------------------
# VAT challenge 
#------------------------------------------------------------------------

# item = int(input("What is the price of the item ? £ "))
# print("VAT is 20 %")
# print("So the VAT of your item is £",item / 100 * 20)

#------------------------------------------------------------------------
# CONVERSION CHALLENGE
#------------------------------------------------------------------------

# print("Welcome to the Conversion-Calculator")

# #created the menus for the length 
# metric_length=["'km', 'm' , 'cm'"]
# imperial_length=["'mi', 'ft', 'in'"]

# ##This defines variables from metric to imperial measurements of distance 
# def km_mi():
#     print(leng1/1.6, "miles")
# def m_ft():
#     print(leng1*3.26, "feet")
# def cm_in():
# 	print(leng1/2.54, "inches")

# #This list defines variables from imperial to metric measurements of distance
# def mi_km():
#     print(leng2*1.6, "kilometers")
# def ft_m():
#     print(leng2/3.26, "metres")
# def in_cm():
#     print(leng2*2.54, "centimetres")

# #menu for weights
# metric_mass=["'t','kg', 'g'"]
# imperial_mass=["'stone', 'lb', 'oz'"]

# #this defines variables from metric to imperial in mass
# def t_st():
#     print(mass1*157.47, "stone")
# def kg_lb():
#     print(mass1*2.2, "pounds")
# def g_oz():
#     print(mass1*0.035, "ounces")
# #this defines variables from imperial to metric in mass
# def st_t():
#     print(mass2*0.00635, "tones")
# def lb_kg():
#     print(mass2*0.4536, "kilograms")
# def oz_g():
#     print(mass2*28.35, "grams")


# #creates startup menu
# menu_type=["'Length-1', 'Weight-2', 'Cacpacity-3'"]

# #choose which what to convert
# print(menu_type)
# measure=int(input("Please select what you would like to convert by typing a number:"))

# #starting if statement chain
# if measure==1:
#     #menu to chose from either metric to imperial or vice-versa
#     print("Metric-Imperial - 1\n")
#     print("Imperial-Metric - 2\n")
#     choice=int(input("Choose a conversion by typing a number: "))
#     #If 1 is chosen follows by asking what metric distance to convert
#     if choice== 1:
#         print("Please choose the measurement you want to use.\n")
#         #prints the metric length menu
#         print(metric_length)
#         distance =input("Type an option from the menu: ")

#         #if statements that takes user input to assign a value for leng1
#         #then runs the function
#         if distance=="km":
#             leng1=int(input("Please enter a number to convert: "))
#             print=(km_mi())
#         elif distance=="m":
#             leng1=int(input("Please enter a number to convert: "))
#             print=(m_ft())
#         elif distance=="cm":
#             leng1=int(input("Please enter a number to convert: "))
#             print=(cm_in())
#         else:
#             print("Invalid Entry")

#     #This is the code for the second choice in the program
#     #If 2 is chosen follows by asking what imperial distance to convert
#     if choice== 2:
#         print("Please choose the measurement you want to use.\n")
#         #prints the imperial length menu
#         print(imperial_length)
#         distance2 =input("Type an option from the menu: ")

#         #if statements that takes user input to assign a value for leng2
#         #then runs the function
#         if distance2=="mi":
#             leng2=int(input("Please enter a number to convert: "))
#             print=(mi_km())
#         elif distance2=="ft":
#             leng2=int(input("Please enter a number to convert: "))
#             print=(ft_m())
#         elif distance2=="in":
#             leng2=int(input("Please enter a number to convert: "))
#             print=(in_cm())
#         else:
#             print("Invalid Entry")

# if measure==2:
#     #menu to chose from either metric to imperial or vice-versa
#     print("Metric-Imperial - 1\n")
#     print("Imperial-Metric - 2\n")
#     choice2=int(input("Choose a conversion by typing a number: "))
#     #If 1 is chosen follows by asking what metric distance to convert
#     if choice2== 1:
#         print("Please choose the measurement you want to use.\n")
#         #prints the metric length menu
#         print(metric_mass)
#         weight =input("Type an option from the menu: ")

#         #if statements that takes user input to assign a value for mass1
#         #then runs the function
#         if weight=="t":
#             mass1=int(input("Please enter weight-2a number to convert: "))
#             print=(t_st())
#         elif weight=="kg":
#             mass1=int(input("Please enter a number to convert: "))
#             print=(kg_lb())
#         elif weight=="g":
#             mass1=int(input("Please enter a number to convert: "))
#             print=(g_oz())
#         else:
#             print("Invalid Entry")

#     #This is the code for the second choice in the program
#     #If 2 is chosen follows by asking what imperial mass to convert
#     if choice2== 2:
#         print("Please choose the measurement you want to use.\n")
#         #prints the imperial length menu
#         print(imperial_mass)
#         weight2 =input("Type an option from the menu: ")

#         #if statements that takes user input to assign a value for mass2
#         #then runs the function
#         if weight2=="stone":
#             mass2=int(input("Please enter a number to convert: "))
#             print=(st_t())
#         elif weight2=="lb":
#             mass2=int(input("Please enter a number to convert: "))
#             print=(lb_kg())
#         elif weight2=="oz":
#             mass2=int(input("Please enter a number to convert: "))
#             print=(oz_g())
#         else:
#             print("Invalid Entry")

#----------------------------------------------------------------------
#  Darts challenge
#----------------------------------------------------------------------

# player_score = 501

# print("New game, player starts at 501 score")

# while player_score != 0:
# 	print("Enter the score after 3 darts")
# 	darts = input()
# 	darts = int(darts)

# 	if player_score - darts > 1:
# 		player_score = player_score - darts
# 		print(player_score)

# 	elif player_score - darts ==0:
# 		print("Your score = 0! You win")
# 		break


#------------------------------------------------------------------------
#  Darts 2
#--------------------------------------------------------------------

# player_1score = 501
# player_2score = 501
# player1count = 0 
# player2count = 0

# print("Player1, throw your darts first and i will reocord how many attempts it took you.")

# while player_1score != 0:
# 	print("player 1, Enter the score after 3 darts")
# 	darts = input()
# 	darts = int(darts)

# 	if player_1score - darts > 1:
# 		player_1score = player_1score - darts
# 		print(player_1score)
# 		player1count = player1count + 1

# 	elif player_1score - darts ==0:
# 		print("Your score = 0!")
# 		player1count = player1count + 1
# 		break

# print("Player2, Now throw your darts and i will record how many attempts it took you")
		
# while player_2score != 0:
# 	print("Player 2, Enter the score after 3 darts")
# 	darts = input()
# 	darts = int(darts)

# 	if player_2score - darts > 1:
# 		player_2score = player_2score - darts
# 		print(player_2score)
# 		player2count = player2count + 1

# 	elif player_2score - darts ==0:
# 		print("Your score = 0!")


# 		if player1count > player2count:
# 			difference1 = player1count - player2count
# 			print("Player 2 wins, As it took you",difference1,"Attempt(s) less.")
# 			break
# 		else:
# 			difference2 = player2count - player1count
# 			print("Player 1 wins, As it took you",difference2,"Attempt(s) less.")
# 			break

#---------------------------------------------------------------------
# Snakes eye challenge
#-------------------------------------------------------------------
















