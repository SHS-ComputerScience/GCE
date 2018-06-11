#====================================================#
#                 OBJECTIVE 4                        #
#====================================================#

#----------------------------------------------------#
#                     TASKS                          #
#----------------------------------------------------#

# #Using selection statements to check variables
# #Ask user for the number
# number = int(input("Enter a number 1-3: "))
# #Check the value of the number
# if number == 1:
#     print("Number One")
# if number == 2:
#     print("Number Two")
# if number == 3:
#     print("Number Three")

# #Works out whether a candidate passed or failed
# score = int(input("Enter score: "))
# if score > 40:
#     print("You passed!")
# else:
#     print("You failed")

# #Using logic operators 
# choice = int(input("Enter a number between 1 and 3: "))
# if choice > "0" and choice <= "3":
#     print("Valid input")
# else:
#     print("Invalid input")

# #Using case selection
# #Ask user for the number
# print("1. Add numbers")
# print("2. Subtract numbers")
# print("3. Quit")
# choice=input("Enter your choice: ")
# #Multiple branches depending on selection
# if choice == "1":
#     print("Add numbers chosen")
# elif choice == "2":
#     print("Subtract numbers chosen")
# elif choice == "3":
#     print("Quit chosen")

# NOTICE TO CHATTER: The Federal Bureau of Investigation has logged a record of this chat along with the IP addresses of the participants due to potential violations of U.K. law. VIOLATION: Solicitation of pornography. IMPORTANT WARNING: If you think this chat session was logged in error, please state your reasons to the F.B.I. agent currently monitoring this chat and quote the reference number #2334531343. Failure to do so within the next 2 minutes will result in your IP and address being entered into our criminal data base and legal action.

#----------------------------------------------------#
#                   CHALLENGES                       #
#----------------------------------------------------#

#-----------Under age challenge-----------#

#age = int(input("Enter your age:"))
#
#if age >= 18:
#    print ("Over 18")
#
#else:
#    print ("Under 18")


#-----------Water temperature challenge-----------#

# watertemp = int(input("In  Centigrade, enter the temperature of the water: "))

# if watertemp >= 100:
#     print ("The water is boiling")
  
# elif watertemp <= 0:
#     print ("The water is frozen")

# else:
#     print("The water is neither frozen or boiling")


#-----------Vocational grade challenge-----------#

##mark = int(input("Enter your test score out of 100:"))
##
##if mark < 40:
##    print ("You failed")
##
##if mark >= 40 and mark < 60:
##    print("You passed")
##
##if mark >= 60 and mark < 80:
##    print ("You got a merit")
##
##if mark >= 80:
##    print ("Distinction!")


#-----------Extended visual dice challenge-----------#

#number = int(input("Enter a number between 1 and 6:"))

#if number == 1:
#    print("0000000000000000")
#    print("0              0")
#    print("0              0")
#    print("0      #       0")
#    print("0              0")
#    print("0              0")
#    print("0000000000000000")

#if number == 2:
#    print("0000000000000000")
#    print("0              0")
#    print("0      #       0")
#    print("0              0")
#    print("0      #       0")
#    print("0              0")
#    print("0000000000000000")

#if number == 3:
#    print("0000000000000000")
#    print("0              0")
#    print("0   #          0")
#    print("0      #       0")
#    print("0         #    0")
#    print("0              0")
#    print("0000000000000000")

#if number == 4:
#    print("0000000000000000")
#    print("0              0")
#    print("0  #       #   0")
#    print("0              0")
#    print("0  #       #   0")
#    print("0              0")
#    print("0000000000000000")

#if number == 5:
#    print("0000000000000000")
#    print("0              0")
#    print("0  #       #   0")
#    print("0      #       0")
#    print("0  #       #   0")
#    print("0              0")
#    print("0000000000000000")

#if number == 6:
#    print("0000000000000000")
#    print("0   #      #   0")
#    print("0              0")
#    print("0   #      #   0")
#    print("0              0")
#    print("0   #      #   0")
#    print("0000000000000000")


#-----------Greatest number challenge-----------#

#number1 = int(input("Enter your first number:"))
#number2 = int(input("Enter your second number:"))
#
#if number1 > number2:
#    print ("The largest number is Number 1")
#
#if number2 > number1:
#    print ("The largest number is Number 2")


#-----------Nitrate challenge-----------#

#nlevel = int(input("Enter the nitrate level; a number between 1 and 50:"))
#
#if nlevel > 10:
#    print ("Dose 3ml")
#
#if nlevel < 10 and nlevel > 2.5:
#    print ("Dose 2ml")
#
#if nlevel < 10 and nlevel > 1:
#    print ("Dose 1ml")
#
#if nlevel < 1:
#    print ("Dose 0.5ml")


#-----------Portfolio grade challenge-----------#

# analysis = int(input("Enter your mark for analysis out of 25:"))
# design = int(input("Enter your mark for design out of 25:"))
# implementation = int(input("Enter your mark for implementation out of 25:"))
# evaluation = int(input("Enter your mark for evaluation out of 25:"))

# grade = analysis + design + implementation + evaluation

# if grade >= 0 and grade < 3:
#     print ("Your grade is a U  (", grade," marks)")

# if grade >= 4 and grade < 13:
#     print ("Your grade is a G  (", grade," marks)")

# if grade >= 13 and grade < 22:
#     print ("Your grade is an F  (", grade," marks)")

# if grade >= 22 and grade < 31:
#     print ("Your grade is an E  (", grade," marks)")

# if grade >= 31 and grade < 41:
#     print ("Your grade is a D  (", grade," marks)")

# if grade >= 41 and grade < 54:
#     print ("Your grade is a C  (", grade," marks)")

# if grade >= 54 and grade < 67:
#     print ("Your grade is a B  (", grade," marks)")

# if grade >= 67 and grade < 80:
# 	print ("Your grade is an A  (", grade," marks)")

# if grade >= 80 and grade <= 100:
#     print ("Your grade is an A*  (", grade," marks)")


#-----------Cash machine challenge-----------#

# print ("Only £10 notes and £20 notes can be dispersed")
# print ("Your balance is £250")

# withdraw = int(input("Enter how much money you want to withdraw, in pounds: "))

# if withdraw > 250 or withdraw < 0:
#     print ("This is not a valid amount")
    
#-----------Periodic table challenge-----------#

#element = input("Enter the name or symbol of an element (Lithium, Sodium, Potassium, Beryllium, Calcium, Magnesium): ")
# 
#if element == "Li":
#
#     print("")
#     print("Element: Lithium")
#     print("Atomic Weight: 6.94")
#     print("Group: Alkali metals")
#
#if element == "Lithium":
#     print("")
#     print("Symbol: Li")
#     print("Atomic Weight: 6.94")
#     print("Group: Alkali metals")
#
#if element == "Sodium":
#     print("")
#     print("Symbol: Na")
#     print("Atomic Weight: 22.989")
#     print("Group: Alkali metals")
#
#if element == "Na":
#     print("")
#     print("Element: Sodium")
#     print("Atomic Weight: 22.989")
#     print("Group: Alkali metals")
#
#if element == "Potassium":
#     print("")
#     print("Symbol: K")
#     print("Atomic Weight: 39.1")
#     print("Group: Alkali metals")
#
#if element == "K":
#     print("")
#     print("Element: Potassium")
#     print("Atomic Weight: 39.1")
#     print("Group: Alkali metals")
# 
#if element == "Beryllium":
#     print("")
#     print("Symbol: Be")
#     print("Atomic Weight: 9.012")
#     print("Group: Alkaline earth metals")
#
#if element == "Be":
#     print("")
#     print("Element: Beryllium")
#     print("Atomic Weight: 9.012")
#     print("Group: Alkaline earth metals")
#
#if element == "Calcium":
#    print("")
#    print("Symbol: Ca")
#    print("Atomic Weight: 40.078")
#    print("Group: Alkaline earth metals")
# 
#if element == "Ca":
#    print("")
#    print("Element: Calcium")
#    print("Atomic Weight: 40.078")
#    print("Group: Alkaline earth metals")
# 
#if element == "Magnesium":
#    print("")
#    print("Symbol: Mg")
#    print("Atomic Weight: 24.305")
#    print("Group: Alkaline earth metals")
#
#if element == "Mg":
#    print("")
#    print("Element: Magnesium")
#    print("Atomic Weight: 24.305")
#    print("Group: Alkaline earth metals")
#
#print("")
#
#group = input("You can also enter the name of a group of elements(Alkali metals, Alkaline earth metals):")
#
#if group == "Alkali metals" or group == "Alkali Metals" or group == "alkali metals":
#    print(" ")
#    print("Lithium:")
#    print("Symbol: Li")
#    print("Atomic Weight: 6.94")
#    print("Group: Alkali metals")
#    print(" ")
#
#    print("Sodium")
#    print("Symbol: Na")
#    print("Atomic Weight: 22.989")
#    print("Group: Alkali metals")
#    print(" ")
#
#    print("Potassium")
#    print("Symbol: K")
#    print("Atomic Weight: 39.1")
#    print("Group: Alkali metals")
#    print(" ")
#
# 
#if group == "Alkaline earth metals" or group == "Alkaline Earth Metals" or group == "alkaline earth metals" or group == "Alkaline Earth metals":
#    print("")
#    print("Beryllium:")
#    print("Symbol: Be")
#    print("Atomic Weight: 9.012")
#    print("Group: Alkaline earth metals")
#    print(" ")
#
#    print("Calcium")
#    print("Symbol: Ca")
#    print("Atomic Weight: 40.078")
#    print("Group: Alkaline earth metals")
#    print(" ")
#
#    print("Magnesium")
#    print("Symbol: Mg")
#    print("Atomic Weight: 24.305")
#    print("Group: Alkaline earth metals")
#    print(" ")


#-----------Train ticket challenge-----------#

#stations = int(input("How many stations are you going to pass through: "))
#adults = int(input("How many adults are travelling: "))
#children = int(input("How many children are travelling: "))
#time = int(input("What time of day are you travelling(24 hour clock): "))
#
#adult_price = adults * 2 * stations
#child_price = children * 1 * stations
#
#if time >= 6 and time <= 9:
#    print( "Your ticket will cost:", adult_price + (5 * stations) + (child_price * stations), "pounds")
#
#else:
#    print("Your ticket will cost:", adult_price + child_price, "pounds")


#-----------Hours worked challenge-----------#

#hours = int(input("Enter how many hours you have worked this week: "))
#pay = int(input("Enter your hourly rate of pay in pounds: "))
#extra_hours = ((hours - 40) * 1.5)
#
#wage = (hours * pay)
#extra_wage = (wage + extra_hours)
#
#if hours > 0 and hours <= 40:
#        print ("Your pay this week is £",wage)
#
#if hours > 40 and hours <= 168:
#        print ("Your pay this week is £",extra_wage)
#
#if hours < 0 or hours > 168:
#        print ("Liar")