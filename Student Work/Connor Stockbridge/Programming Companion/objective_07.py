#                   Objective 7 - Connor Stockbridge - 18/10/2017
#---------------------------------Menu Selection Challenge-----------------------
print('-------Menu-------')
print('1 - PLay Game')
print('2 - Instructions')
print('3 - Quit')
counter = 0
user = int(input('Pick Your Option:'))
if user == 1 or user == 2 or user == 3:
   print('You Selected',user,'Let`s Go')

else:
   print('Option Not Avaliable')
#---------------------------------Compound interest challenge-----------------------
staBalance = int(input('What is your account balance:'))
time = int(input('How many years do you plan to use this bank?:'))
subBalance = staBalance
counter = 0

for i in range(0,time):
   newBalance = subBalance + (subBalance*0.04)
   subBalance = newBalance
   counter = counter + 1
   print('Year',counter,': New Balance =',subBalance)
#---------------------------------Guess the number game challenge-----------------------
import random

comValue = random.randint(0,100)
counter = 0

for i in range(0,100):
   usersValue = int(input('What is my number?:'))
   counter = counter + 1
   if usersValue < comValue:
       print('Thats Too Low.')

   elif usersValue > comValue:
       print('Thats Too HIgh')

   elif usersValue == comValue:
       print('You Got It!')
       print('It Took You',counter,'Guesses.')
       break
#-----------------------------------------Gamertag challenge-----------------------------
gamertag = input('Please enter your Gamertag:')
tag_len = int(len(gamertag))

if tag_len <= 15:
   print('The Gamertag',gamertag,',is avalible')

else:
   print('Thats not a valid name.')
#-----------------------------------------Rock, paper, scissors challenge-----------------------------
import random
comScore = 0
player1 = 0


def base_game():
   global comScore
   global player1
while comScore != 10 or player1 != 10:
   pc_move = random.randint(1,3)
   print('Pick your move: 1 - Rock')
   print('                2 - Paper')
   print('                3 - Scissors')
   player_move = int(input('You Move:'))
   if player_move >= 4 or player_move < 0:
       print('Thast not a vaild move.')
   elif pc_move == player_move:
       print('Draw')
       print('COM -',comScore)
       print('Player 1 -',player1)
   elif (pc_move == 1 and player_move == 3) or (pc_move == 3 and player_move == 2) or (pc_move == 2 and player_move == 1):
       print('Com Wins')
       comScore = comScore + 1
       print('COM -',comScore)
       print('Player 1 -',player1)
   elif (pc_move == 3 and player_move == 1) or (pc_move == 2 and player_move == 3) or (pc_move == 1 and player_move == 2):
        print('Player 1 Wins')
        player1 = player1 + 1
        print('COM -',comScore)
        print('Player 1 -',player1)

def end_game():
   if comScore == 10:
       print('YOU LOSE')
   

   elif player1 == 10:
       print('YOU WIN')
       

if comScore == 10 or player1 == 10:
   base_game()

elif comScore == 10 or player1 == 10:
   end_game()
#-----------------------------------------Happy numbers challenge-----------------------------
number = int(input("Enter a number to check if it is happy: "))
number_split = set()
while 1:
  if number == 1:
      print("Number is happy!")
      break
  number = sum(int(c) ** 2 for c in str(number))
  if number in number_split:
      print("Number is sad!")
      break
  number_split.add(number)
#-----------------------------------------XP Challenge-----------------------------
XP = 0
Player_rank = 1

while XP < 2000:
    XP = XP + int(input('How much XP did you earn last game:'))
    if XP >= 100:
        Player_rank = Player_rank + 1
        print('You have been promoted to Corporal.')
        print('Rank increased to',Player_rank)
        print('Your Total XP is',XP)
    if XP >= 200:
        Player_rank = Player_rank + 1
        print('You have been promoted to Sergeant.')
        print('Rank increased to',Player_rank)
        print('Your Total XP is',XP)
    if XP >= 300:
        Player_rank = Player_rank + 1
        print('You have been promoted to Staff Sergeant.')
        print('Rank increased to',Player_rank)
        print('Your Total XP is',XP)
    if XP >= 700:
        Player_rank = Player_rank + 1
        print('You have been promoted to Warrent Officer.')
        print('Rank increased to',Player_rank)
        print('Your Total XP is',XP)