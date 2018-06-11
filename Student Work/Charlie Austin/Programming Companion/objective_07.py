#-----------------------------------------------------------------------------------
#                                       TASKS
#-----------------------------------------------------------------------------------



###Program to add up numbers until 0 is entered
##
##total=0
##number=1
##
##while number>0:
##    number=int(input("Enter a number: "))
##    total=total+number
##
##print("The sum of the numbers is:",total)




#-----------------------------------------------------------------------------------
#                              MENU SELECTION CHALLENGE
#-----------------------------------------------------------------------------------



##print("Select one option:")
##print("")
##
##print("1. Play Game")
##print("2. Instructions")
##print("3. Quit")
##
##choice = input("Select choice: ")
##
##if choice == "1":
##    print("Lets Go!")
##if choice == "2":
##    print("Press 1 to play or press 3 to quit")

    






#-----------------------------------------------------------------------------------
#                               COMPOUND INTEREST CHALLENGE
#-----------------------------------------------------------------------------------




##balance = int(input("Enter your bank balance: "))
##interest = int(input("Enter the interest rate: "))
##future_balance = int(input("How much money would you like to get to: "))
##
##
##year = 0
##
##interest_rate = (interest / 100)
##
##while balance < future_balance:
##   year = year + 1
##   balance = balance + (balance * interest_rate)
##   print("year",year,"balance = ", balance)



#-----------------------------------------------------------------------------------
#                         GUESS THE NUMBER GAME CHALLENGE
#-----------------------------------------------------------------------------------
   

##import random
##
##guessesTaken = 0
##
##
##number = random.randint(1, 100)
##print('I am thinking of a number between 1 and 100.')
##
##while guessesTaken < 101:
##   print('Take a guess.') 
##   guess = input()
##   guess = int(guess)
##
##   guessesTaken = guessesTaken + 1
##
##   if guess < number:
##         print('Your guess is too low.') 
##
##   if guess > number:
##         print('Your guess is too high.')
##
##   if guess == number:
##         break
##
##if guess == number:
##   guessesTaken = str(guessesTaken)
##   print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')
##
##if guess != number:
##   number = str(number)
##   print('Nope. The number I was thinking of was ' + number)




#-----------------------------------------------------------------------------------
#                                 GAMERTAG CHALLENGE
#-----------------------------------------------------------------------------------



##print("This program checks the lenghts of entered gamertags")
##print("")
##
##
##
##print("Gamertags must be a maximum of 15 characters long")
##print("")
##
##gamertag = input("Enter gamertag: ")
##
##gamertag_length = gamertag.len()
##
##while gamertag_length > 15:
##   print("Gamertag invalid, please enter a new one: ")
##
##if gamertag_length <= 15:
##   print("Valid gamertag:",gamertag)



#-----------------------------------------------------------------------------------
#                                  ROCK, PAPER, SCISSORS
#-----------------------------------------------------------------------------------




##import random
##
##choices = ["rock", "paper", "scissors"]
##computer = random.choice(choices)
##
##player = input("Rock, Paper or Scissors: ")
##
##print("Computer chose",computer)
##print("")
##
##
##if computer == "rock" and player == "scissors":
##   print("You lose, rock beats scissors")
##if computer == "scissors" and player == "rock":
##   print("You win, rock beats scissors")
##
##if computer == "scissors" and player == "paper":
##   print("You lose, scissors beats paper")
##if computer == "paper" and player == "scissors":
##   print("You win, scissors beats paper")
##
##if computer == "paper" and player == "rock":
##   print("You lose, paper beats rock")
##if computer == "rock" and player == "paper":
##   print("You win, paper beats rock")



#-----------------------------------------------------------------------------------
#                               HAPPY NUMBERS CHALLENGE
#-----------------------------------------------------------------------------------


##number = int(input("Enter a number to check if it is happy: "))
##number_split = set()
##while 1:
##    if number == 1:
##        print("Number is happy!")
##        break
##    number = sum(int(c) ** 2 for c in str(number))
##    if number in number_split:
##        print("Number is sad!")
##        break
##    number_split.add(number)




#-----------------------------------------------------------------------------------
#                                   XP CHALLENGE
#-----------------------------------------------------------------------------------


		
# XP = 0
# Player_rank = 1

# while XP < 2000:
#    XP = XP + int(input('How much XP did you earn last game:'))
#    if XP >= 100 and XP < 200:
#        Player_rank = Player_rank + 1
#        print('You have been promoted to Corporal.')
#        print('Rank increased to',Player_rank)
#        print('Your Total XP is',XP)
#    if XP >= 200 and XP < 300:
#        Player_rank = Player_rank + 1
#        print('You have been promoted to Sergeant.')
#        print('Rank increased to',Player_rank)
#        print('Your Total XP is',XP)
#    if XP >= 300 and XP < 700:
#        Player_rank = Player_rank + 1
#        print('You have been promoted to Staff Sergeant.')
#        print('Rank increased to',Player_rank)
#        print('Your Total XP is',XP)
#    if XP >= 700:
#        Player_rank = Player_rank + 1
#        print('You have been promoted to Warrent Officer.')
#        print('Rank increased to',Player_rank)
       print('Your Total XP is',XP)