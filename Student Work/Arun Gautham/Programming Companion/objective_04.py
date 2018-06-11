#OBJECTIVE 4
#1.
#Using selection statements to check variable
#Ask user for the number
number = int(input("Enter a number 1-3:")
#Check the value of the number 
if number == 1: print("Number one")
if number == 2: print("Number two")
if number == 3: print("Number three")

#2.
#Works out whether a candidate passed or failed 
score = int(input("Enter score:"))
if score > 40:
print("You passed")
else:
print("You failed")

#3.
score = int(input("Enter score:"))
if score > 50:
print("You passed")
else:
print("You failed")

#4.
#Returns whether two numbers are the same
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 != num2: print("The numbers are not the same") 
else:
print("The numbers are the same")

#5.
#Using logic operators
choice = input("Enter a number 1-3: ")
if choice > "0" and choice < "3":
print("Valid input") else:
print("Invalid input")

#6.
#Using case selection
#Ask user for the number
print("1. Add numbers")
print("2. Subtract numbers")
print("3. Quit") 
choice=input("Enter your choice: ")
#Multiple branches depending on selection
if choice == "1":
print("Add numbers chosen")
elif choice == "2":
print("Subtract numbers chosen")
elif choice == "3":
print("Quit chosen") 

#CHALLENGES
             
#Under age challenge 
age = int(input("Whats ur age?"))
if age > 18:
    print("You are over 18")
else:
    print("You are under 18")
             
#Water temperature challenge
temp = int(input("The temperature in centigrade is: "))
if temp <= 0:
    print("Water is frozen")
if temp >= 100:
    print("Water is boiling")
if temp <100 and temperature >0:
    print("Water is not frozen or boiling")

#Vocational grade challenge
mark = int(input("Enter the mark out of 100: "))
if mark <40:
    print("Fail :(")
if mark >40 and score <60:
    print("PASS :)")
if mark >60 and score <80:
    print("Merit :) :)")
if mark >80 and score <=100:
    print("Distinction :) :) :)")
if mark >100:
    print("Invalid mark")

#Greatest number challenge
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Number 1 is bigger")
if num1 < num2:
    print("Number 2 is bigger")
if num1 == num2:
    print("Both numbers are the same")

#Nitrate challenge
nitrate = int(input("Input the nitrate level of the fish tank between 1-50? "))

if nitrate > 10 and nitrate <=50:
    print("Add a dose of 3ml of carbon to the tank")
if nitrate > 2.5 and nitrate < 10:
    print("Add a dose of 2ml of carbon to the tank")
if nitrate > 1 and nitrate < 2.5:
    print("Add a dose of 1ml of carbon to the tank")
if nitrate < 1 and nitrate > 0:
    print("Add a dose of 0.5ml of carbon to the tank")
if nitrate > 50:
    print("Invalid level of nitrate")

#Portfolio grade challenge
ana = int(input("Enter your analysis mark out of 25 "))
des = int(input("Enter your design mark out of 25 "))
imp = int(input("Enter your implementation mark out of 25 "))
eva = int(input("Enter your evaluation mark out of 25 "))

totalMark = print("Your total mark is: ",ana + des + imp + eva)

if totalMark < 4:
    print("You acheived an U")    
if  totalMark >=4 and total_mark <13:
    print("You acheived an G")   
if totalMark >=13 and total_mark <22:
    print("You acheived an F")    
if totalMark >=22 and total_mark <31:
    print("You acheived an E")    
if totalMark >=31 and total_mark <41:
    print("You acheived an D")    
if totalMark >=41 and total_mark <54:
    print("You acheived an C")    
if totalMark >=54 and total_mark <67:
    print("You acheived an B")    
if totalMark >=67 and total_mark <80:
    print("You acheived an A")   
if totalMark >=80 and total_mark <=100:
    print("You acheived an A*")
             
#Cash machine challenge
print("Balance: £250")
print("")

print("How much cash would you like to withdraw?")
print("")

print('''
1. £10
2. £50
3. £100
4. £150
5. £200
6. £250
7. Custom amount
'''

choice = input("Input choice: ")
if choice == "1":
    print("Dispensing £10 in 1 £10 note and your new balance is £240")
if choice == "2":
    print("Dispensing £50 in 2 £20 notes and 1 £10 note and your new balance is £200")
if choice == "3":
    print("Dispensing £100 in 5 £20 notes and your new balance is £150")
if choice == "4":
    print("Dispensing £150 in 7 £20 notes and 1 £10 note and your new balance is £100")
if choice == "5":
    print("Dispensing £200 in 10 £20 notes and your new balance is £50")
if choice == "6":
    print("Dispensing £250 in 12 £20 notes and 1 £10 note and your new balance is £0")

print("")

if choice == "1":
    print("New balance = £240")
if choice == "2":
    print("New balance = £200")
if choice == "3":
    print("New balance = £150")
if choice == "4":
    print("New balance = £100")
if choice == "5":
    print("New balance = £50")
if choice == "6":
    print("New balance = £0")
      
#Train ticket challenge
print("You are taking a train from Cheltenham to London")
print("")
adults = int(input("How many adults are there: "))
children = int(input("How many children are there: "))

stations = int(input("How many stations are you passing through: "))
time = int(input("What hour of day are you travelling at? (24 hour): "))

adultFare = adults * stations * 20
childFare = children * stations * 10

finalFare = adultFare + childFare

if time >= 6 and time <=9:
    stations * 5 + finallFare

print(finalFare)
      
#Hours worked challenge
hours = int(input("How many hours have you worked this week: "))
pay = int(input("How much are you payed per hour: "))

basePay = hours * pay

if hours > 40 and hours < 60:
    (hours - 40) * 1.5 + basePay

print(basePay)






