#OBJECTIVE 7
##
###Program to add up numbers until 0 is entered
##
##total=0
##number=1
##while number>0:
## number=int(input("Enter a number: "))
## total=total+number
##print("The sum of the numbers is:",total)


###Menu Selection Challenge
##
##
##
##print("1. Play Game")
##print("2. Instructions")
##print("3. Quit")
##
##option = int(input("Please choose what you would like to do and enter the corresponding number."))
##
##while option>3:
## print("1. Play Game")
## print("2. Instructions")
## print("3. Quit")
## option = int(input("Please choose what you would like to do and enter the corresponding number."))
##
##
##while option<1:
## print("1. Play Game")
## print("2. Instructions")
## print("3. Quit")
## option = int(input("Please choose what you would like to do and enter the corresponding number."))
##
##
##if option>=1 and option<=3:
## print("Let's Go!") 
##


##
###COMPOUND INTEREST CHALLENGE 
##
##current_balance = float(input("Please enter your current balance. £"))
##interest_rate = float(input("What is your interest rate as a decimal? For example, 0.04."))
##desired_balance = float(input("What is your desired balance? £"))
##count = 0
##
##while current_balance < desired_balance:
##  count = count + 1
##  interest = current_balance * interest_rate
##  current_balance = current_balance + interest
##  print("Year",count,"£",current_balance) 
##
##print("You will reach your desired balance in",count,"years.") 



###GUESS THE NUMBER GAME CHALLENGE
##
##import random
##random_number = random.randint(1,100)
##count = 1 
##
##guess = int(input("Guess the random number from 1-100."))
##
##
##while guess != random_number:
##
##    if guess < random_number:
##      count = count + 1 
##      print("You guessed too low.")
##      guess = int(input("Guess the random number from 1-100."))
##
##    if guess > random_number:
##      count = count + 1
##      print("You guessed too high.")
##      guess = int(input("Guess the random number from 1-100."))
##
##
##print("You got it!")
##print("You took",count,"times to guess the number correctly.") 
##


###GAMERTAG CHALLENGE 
##
##
##gamertag = input("Please choose your gamertag.  It should be between 5 and 15 characters in length.")
##
##while len(gamertag) < 5 or len(gamertag) > 15:
##
##    if(len(gamertag) > 15):
##        msg = "longer than 15 characters."
##    else:
##        msg = "shorter than 5 characters."
##        
##    print("Your gamertag cannot be " , msg , "Please choose another.")
##    gamertag = input("Please choose your gamertag.")
##    
##print("Welcome",gamertag) 
##


###ROCK, PAPER, SCISSORS CHALLENGE
##
##rock = 1
##paper = 2
##scissors = 3
##
##count = 0
##
##computer_option = radint(1,3) 
##option = input("Please choose rock, paper or scissors.")
##
##
##
##
##while count < 10
## 
## if option == 1:
##     count = count + 1
##  print("Rock beats scissors!")
##
##
## if option == 2:
##     count = count + 1
##  print("Paper beats rock!")
##
## if option == 3:
##     count = count + 1
##  print("Scissors beats paper!")

 
###ROCK, PAPER, SCISSORS CHALLENGE
##
##import random
##
##user_score = 0
##comp_score = 0
##
##options=["rock","paper","scissors"]
##
##user_option = input("Rock, Paper or Scissors?").lower()
##computer_option = random.choice(options)
##
##
##while user_score < 10 and comp_score < 10: 
##    if (user_option==computer_option):
##        user_score +=1
##        comp_score +=1
##        print("It's a draw.")
##    elif ((user_option=="rock") and (computer_option=="scissors")):
##        user_score +=1
##        print("Rock beats scissors. You win!")
##    elif ((user_option=="paper") and (computer_option=="rock")):
##        user_score +=1
##        print("Paper beats rock. You win!")
##    elif ((user_option=="scissors") and (computer_option=="paper")):
##        user_score +=1
##        print("Scissors beats paper. You win!")
##    else:
##        comp_score +=1
##        print("You lose!")
##    print("You said: " + user_option)
##    print("The computer chose: " + computer_option)
##
##    print("The score is",user_score," - ",comp_score)
##    computer_option = random.choice(options)
##    user_option = input("Rock, Paper or Scissors?").lower()
##    
##if comp_score > user_score:
## print("You lose!")
##else:
##    print("You win!")


#HAPPY NUMBERS CHALLENGE 






###XP Challenge
##
##xp = 0
##score = 0
##
##while score <= 2000:
##
##     xp = int(input("What XP did you earn in your most recent game?"))
##     score += xp
##     
##     if score <= 100:
##      print("You now rank as a Private")
##      print("Your current XP is now", score)
##         
##
##     elif score <= 300:
##      print("You now rank as a Corporal")
##      print("Your current XP is now", score)
##    
## 
##     elif score <= 700:
##      print("You now rank as a Sergeant")
##      print("Your current XP is now", score)
##
##     elif score <= 1500:
##         print("You now rank as a Staff Sergeant") 
##         print("Your current XP is now", score)
##    
##     else:
##           print("You now rank as a Warrant Officer")
##           print("Your current XP is now", score)
##            
##
##if score >= 2000:
##          print("Congratulations, you have completed the game.")    
 

