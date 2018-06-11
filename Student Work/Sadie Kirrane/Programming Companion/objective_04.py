###Under Age Challenge
##
##age = int(input("How old are you?"))
##if age<= 18:
##  print("Under 18")
##else :
## print("Over 18")



###Water Temperature Challenge
##
##
##temp = int(input("What is the temperature of the water in degrees Centigrade?"))
##if (0<temp and temp<100):
## print(" The water is neither boiling nor freezing.") 
##if (0>temp):
## print(" The water is freezing.") 
##if (temp>100):
## print(" The water is boiling.")


###Vocational Grade Challenge
##
##grade = int(input("What was your grade out of 100?"))
##if (grade<40):
##    print("FAIL")
##if (40<grade and grade<60):
##    print("PASS")
##if (60<grade and grade<80):
##    print("MERIT")
##if (80<grade):
##    print("DISTINCTION")


###Extended Visual Dice Challenge
##
##number = int(input("Please choose a number between 1-6."))
##if number==1:
## print("0000000000")
## print("0        0")
## print("0        0")
## print("0   #    0")
## print("0        0")
## print("0        0")
## print("0000000000")
##
##if number==2:
## print("0000000000")
## print("0        0")
## print("0   #    0")
## print("0        0")
## print("0    #   0")
## print("0        0")
## print("0000000000")
## 
##if number==3: 
## print("0000000000")
## print("0 #      0")
## print("0        0")
## print("0   #    0")
## print("0        0")
## print("0     #  0")
## print("0000000000")
## 
##if number==4: 
## print("0000000000")
## print("0 #   #  0")
## print("0        0")
## print("0        0")
## print("0        0")
## print("0 #    # 0")
## print("0000000000")
## 
##if number==5:
## print("0000000000")
## print("0 #   #  0")
## print("0        0")
## print("0    #   0")
## print("0        0")
## print("0 #    # 0")
## print("0000000000")
## 
##if number==6:
## print("0000000000")
## print("0 #   #  0")
## print("0        0")
## print("0 #   #  0")
## print("0        0")
## print("0 #    # 0")
## print("0000000000")


###Greatest Number Challenge
##
##number_one = int(input("Please input a number.")) 
##number_two = int(input("Please input another number."))
##
##if (number_one>number_two):
##         print("The larger number is the first number")
##if (number_one<number_two):
##         print("The larger number is the second number")

##
###Nitrate Challenge
##
##nitrate = int(input("What is the level of nitrate in the fish tank? Pick a number between 1-50."))
##if (50>nitrate>10):
##    print("Dose 3ml of carbon")
##if (10>nitrate>2.5):
##    print("Dose 2ml of carbon")
##if (1<nitrate<2.5):
##    print("Dose 1ml of carbon")
##if (nitrate<1):
##    print("Dose 0.5ml of carbon")
    
##
###Portfolio Grade Challenge
##
###Cash Machine Challenge
##balance = int(250) 
##print("Your balance is £250")
##withdrawal = int(input("How much would you like to withdraw?"))
##if (withdrawal<balance):
##    print("This is acceptable.")
##    print(withdrawal,"is being withdrawn.")
##    new_balance = (balance - withdrawal)
##    print("Your current balance is now £",new_balance,".") 
##
##    
##if (withdrawal>balance):
##    print("You cannot withdraw this amount. Select another option.") 





### Hourly Pay Challenge 
##
##hours_worked = int(input("How many hours have you worked this week?")) 
##hourly_pay = int(input("What is your hourly rate of pay?"))
##                       
##extra_hours = ((hours_worked - 40) * 1.5)
##gross_wage = (hours_worked * hourly_pay)
##extra_wage = (gross_wage + extra_hours) 
##
##if hours_worked > 0 and hours_worked < 60:
##       print("Your weekly wage is £",extra_wage,".") 
##
##
##else :
##    print("ERROR") 
##

#Periodic Table Challenge 

##group = input("You can also enter the name of a group of elements(Alkali metals, Alkaline earth metals):")
##
##if group == "Alkali metals" or group == "Alkali Metals" or group == "alkali metals":
##    print(" ")
##    print("Lithium:")
##    print("Symbol: Li")
##    print("Atomic Weight: 6.94")
##    print("Group: Alkali metals")
##    print(" ")
##
##    print("Sodium")
##    print("Symbol: Na")
##    print("Atomic Weight: 22.989")
##    print("Group: Alkali metals")
##    print(" ")
##
##    print("Potassium")
##    print("Symbol: K")
##    print("Atomic Weight: 39.1")
##    print("Group: Alkali metals")
##    print(" ")
##
## 
##if group == "Alkaline earth metals" or group == "Alkaline Earth Metals" or group == "alkaline earth metals" or group == "Alkaline Earth metals":
##    print("")
##    print("Beryllium:")
##    print("Symbol: Be")
##    print("Atomic Weight: 9.012")
##    print("Group: Alkaline earth metals")
##    print(" ")
##
##    print("Calcium")
##    print("Symbol: Ca")
##    print("Atomic Weight: 40.078")
##    print("Group: Alkaline earth metals")
##    print(" ")
##
##    print("Magnesium")
##    print("Symbol: Mg")
##    print("Atomic Weight: 24.305")
##    print("Group: Alkaline earth metals")
##    print(" ")

##
###Train Ticket Challenge
##
##stations = int(input("How many stations are you going to pass through: "))
##adults = int(input("How many adults are travelling: "))
##children = int(input("How many children are travelling: "))
##time = int(input("What time of day are you travelling(24 hour clock): "))
##
##adult_price = adults * 20 * stations
##child_price = children * 10 * stations
##
##if time >= 6 and time <= 9:
##    print( "Your ticket will cost:", adult_price + (5 * stations) + (child_price * stations), "pounds")
##
##else:
##    print("Your ticket will cost:", adult_price + child_price, "pounds")
