##import random
##numbersides = int(input("Number of sides on dice : "))
##print("you rolled a",random.randint(1,numbersides))

##n1 = int(input("Enter first number"))
##if n1 == 0:    
##    print("ERROR"),exit()
##n2 = int(input("Enter second number"))
##if n2 == 0:    
##    print("ERROR"), exit()
##product = n1%n2
##if product == 0:
##    print(n1, "is exactly divisible by", n2)
##if not product == 0:
##    print(n1, "is NOT exactly divisible by", n2)

##month = int(input("Enter month number between 1-12:",))
##
##if month == 1:
##    print("""Month: January
##Days: 31""")
##
##if month == 3:
##    print("""Month: March
##Days: 31""")
##
##if month == 5:
##    print("""Month: May
##Days: 31""")
##
##if month == 2:
##    input("is it a leap year?")
##    if "Y" or "yes":
##            print("""Month: Febuary
##Days: 29""")
##    else:
##        print("""Month: Febuary
##Days: 28""")
##        
##    if month == 3:
##    print("""Month: March
##Days: 31""")
##
##if month == 6:
##    print("""Month: June
##Days: 30""")
##
##if month == 7:
##    print("""Month: July
##Days: 31""")
##
##if month == 4:
##    print("""Month: April
##Days: 30""")
##
##if month == 8:
##    print("""Month: August
##Days: 31""")
##
##if month == 9:
##    print("""Month: September
##Days: 30""")
##
##if month == 10:
##    print("""Month: October
##Days: 31""")
##
##if month == 11:
##    print("""Month: November
##Days: 30""")
##
##if month == 12:
##    print("""Month: December
##Days: 31""")

import random
nsides1 = int(input("Number of sides on dice one : "))
nsides2 = int(input("Number of sides on dice two: "))
nsides3 = int(input("Number of sides on dice three: "))
score1 = random.randint(1,nsides1)
score2 = random.randint(1,nsides2)
score3 = random.randint(1,nsides3)
print("you rolled the numbers",score1, score2,"and",score3)
if nsides1==nsides2 and nsides1==nsides3 and nsides2==nsides3:
    print("Your score: ", score1 + score2 + score3)
    

if not nsides1==nsides2 or not nsides1==nsides3 or not nsides2==nsides3:
    print("Your score: 0")
    

if nsides1==nsides2:
          print("Your score: ", score1+score2)
          
if nsides1==nsides3:
    print("Your score: ", score1+socre3)

if nsides2==nsides3:
    print("Your score: ", score3+score2)
