"""
===============================================
 PROGRAMMING COMPANION OBJECTIVE 08 (EXEMPLAR)
===============================================

KEY LEARNING POINTS:
 - Subroutines, procedures and functions
 
KEY WORDS:
 - def
 - global
 - return
 
"""

# -----------------------------------------------
#  VAT Challenge
# -----------------------------------------------
# price = int(input('What is the price of the item:'))
# vat = ((price / 1.15) - price) * -1
# print('The added VAT would be',vat)
    
# -----------------------------------------------
#  Conversion Challenge
# -----------------------------------------------

# def opt_1():
#     metric_value = int(input('Enter your length in Meters:'))
#     imperial_value = (metric_value * 1.09361)
#     print('The length',metric_value,'Meters, is',imperial_value,'Yards')

# def opt_2():
#     metric_value = int(input('Enter your mass in Kilogramms:'))
#     imperial_value = (metric_value * 2.2046)
#     print('The mass',metric_value,'Kilogramms, is',imperial_value,'Pounds')

# def opt_3():
#     metric_value = int(input('Enter your temperature in Celcius:'))
#     imperial_value = (metric_value * 9/5) + 32
#     print('The temperature',metric_value,'Celcius, is',imperial_value,'Farenhiet')

# def menu():
#     print('Select Your Conversion:  1 - Length')
#     print('                         2 - Mass')
#     print('                         3 - Temperature')
#     option = int(input('Select:'))
#     return option
    
# opt_selection = menu()

# if opt_selection == 1:
#     opt_1()
    
# elif opt_selection == 2:
#     opt_2()
    
# elif opt_selection == 3:
#     opt_3()
    
# elif opt_selection > 3 or opt_selection < 1:
#     print('Invalid Input')

# -----------------------------------------------
#  Conversion Challenge Part 2
# -----------------------------------------------

# """
# 15 m in yd
# 5 kg in lbs
# 32 c in f
# """

# def m_to_yd(value):
#     return (value * 1.09361, "yds")

# def kg_to_lbs(value):
#     return (value * 2.2046, "lbs")

# def c_to_f(value):
#     return (value * 9/5 +32, "f")
    
# user_input = input("Enter the value followed by the unit:")

# end = -1
# user_list = []

# for i in range(4):
#     start = end + 1
#     space_index = user_input.find(" ", start)
#     if space_index != -1:
#         end = space_index
#     else:
#         end = len(user_input)
#     user_list.append(user_input[start:end])
        
# operand = int(user_list[0])
# original_unit = user_list[1]

# if original_unit == "m":
#     result = m_to_yd(operand)
# elif original_unit == "kg":
#     result = kg_to_lbs(operand)
# elif original_unit == "c":
#     result = c_to_f(operand)

# print(operand, original_unit, "has been converted to", result[0], result[1])

# -----------------------------------------------
#  Darts Challenge
# -----------------------------------------------
# player1_score = 501
# print('New Game. Player Starts at 501 Points')

# while player1_score != 0:
#     scored = int(input('Enter the total from your 3 darts:'))
#     player1_score = player1_score - scored
#     if player1_score < 0:
#             player1_score = player1_score + scored
#             print('Unfortunate Score. Your score is still',player1_score)
#     elif player1_score >= 1:
#         print('Your current score is',player1_score)
#     elif player1_score == 0:
#         print('Player 1 wins the game')
        
# # -----------------------------------------------
# #  Darts Challenge Part 2
# # -----------------------------------------------
# global player1_score
# global player2_score
# global game_selected
# game_selected = 0

# def one_player():
#     player1_score = 501
#     print('New Game. Player Starts at 501 Points')
#     while player1_score != 0:
#         scored = int(input('Enter the total from your 3 darts:'))
#         player1_score = player1_score - scored
#         if player1_score < 0:
#             player1_score = player1_score + scored
#             print('Unfortunate Score. Your score is still',player1_score)
#         elif player1_score >= 1:
#             print('Your current score is',player1_score)
#         elif player1_score == 0:
#             print('Player 1 wins the game')

# def two_player():
#     player1_score = 501
#     player2_score = 501
#     print('New Game.Player 1 Score is',player1_score,'. Player 2 Score is',player2_score)
#     while player1_score != 0 or player2_score != 0:
#             p1_scored = int(input('PLayer 1 - Enter the total from your 3 darts:'))
#             player1_score = player1_score - p1_scored
#             p2_scored = int(input('PLayer 2 - Enter the total from your 3 darts:'))
#             player2_score = player2_score - p2_scored
#             if player1_score < 0:
#                 player1_score = player1_score + p1_scored
#                 print('Unfortunate Score. Your score is still',player1_score)
#             elif player2_score < 0:
#                 player2_score = player2_score + p2_scored
#                 print('Unfortunate Score. Your score is still',player1_score)
#             if player1_score >= 1 and player2_score >= 1:
#                 print('PLayer 1 your current score is',player1_score)
#                 print('PLayer 2 your current score is',player2_score)
#             elif player1_score == 0 or player2_score == 0:
#                 if player1_score == 0:
#                     print('Player 1 wins the game')
#                 if player2_score == 0:
#                      print('Player 2 wins the game')
        
    
        

# def menu():
#     global game_selected
#     print('Select Your Game Mode:  1 - One Player')
#     print('                        2 - Two Player')
#     game_selected = int(input('Select:'))

# menu()

# if game_selected == 1:
#     one_player()

# elif game_selected == 2:
#     two_player()

# else:
#     print('Invalid Input')
   

# # -----------------------------------------------
# #  Snake Eyes Challenge
# # -----------------------------------------------

# p1_bank = 0
# p1_score = 0
# p2_bank = 0
# p2_score = 0
# p1_over = False
# p2_over = False

# def player_1():
#     global p1_bank
#     global p1_score
#     global p2_bank
#     global p2_score
#     global p1_over
#     p1_over = False
#     p1_score = 0
#     roll_1 = random.randint(1,6)
#     roll_2 = random.randint(1,6)
#     p1_score = roll_2 + roll_1

#     if roll_1 == 1 or roll_2 == 1:
#         p1_score = 0
#         print('Your Score Was Reset')
#         print('Score:',p1_score)
#         p1_over = True
#     elif roll_1 == 1 and roll_2 ==1:
#         print('Double Ones`s!!!. YOU LOST EVERYTHING')
#         print('Score:',p1_score)
#         print('Your bank has',p1_bank)
#         bank = o
#         p1_score = 0
#         p1_over = True
#     elif roll_1 != 1 or roll_2 != 1:
#         print('Select Your Move:  1 - Gamble')
#         print('                   2 - Bank')
#         option = int(input('Select:'))
#         if option == 1:
#             print('You Gamble. How Risky')
#             roll_1 = random.randint(1,6)
#             roll_2 = random.randint(1,6)
#             p1_score = roll_2 + roll_1
#         elif option == 2:
#             p1_bank = p1_bank + p1_score
#             print('You Bank')
#             print('Your bank has',p1_bank)
#             p1_score == 0
#             p1_over = True
    
    
# def player_2():
#     global p1_bank
#     global p1_score
#     global p2_bank
#     global p2_score
#     global p2_over
#     p2_over = False
#     p2_score = 0
#     roll_1 = random.randint(1,6)
#     roll_2 = random.randint(1,6)
#     p2_score = roll_2 + roll_1

#     if roll_1 == 1 or roll_2 == 1:
#         p2_score = 0
#         print('Your Score Was Reset')
#         print('Score:',p2_score)
#         p2_over = True
#     elif roll_1 == 1 and roll_2 == 1:
#         print('Double Ones`s!!!. YOU LOST EVERYTHING')
#         print('Score:',p2_score)
#         print('Your bank has',p2_bank)
#         bank = 0
#         p2_score = 0
#         p2_over = True
#     elif roll_1 != 1 or roll_2 != 1:
#         print('Select Your Move:  1 - Gamble')
#         print('                   2 - Bank')
#         option = int(input('Select:'))
#         if option == 1:
#             print('You Gamble. How Risky')
#             roll_1 = random.randint(1,6)
#             roll_2 = random.randint(1,6)
#             p2_score = roll_2 + roll_1
#         elif option == 2:
#             p2_bank = p2_bank + p2_score
#             p2_score == 0
#             print('You Bank')
#             print('Your bank has',p2_bank)
#             p2_over = True

# while p1_bank < 100 and p2_bank < 100:
#     move = random.randint(1,2)
#     if move == 1 or p2_over == True:
#         print('==========PLAYER 1 IT`S YOUR TURN==========')
#         p2_over = False
#         print('PLayer 1')
#         player_1()
#         if p1_bank >= 100:
#             print('==========PLAYER 1 YOU WIN==========')
#     elif move == 2 or p1_over == True:
#         print('==========PLAYER 2 IT`S YOUR TURN==========')
#         p1_over = False
#         print('Player 2')
#         player_2()
#         if p2_bank >= 100:
#             print('==========PLAYER 2 YOU WIN==========')
#         player_2()
#         if p2_bank >= 100:
#             print('==========PLAYER 2 YOU WIN==========')
# # -----------------------------------------------
# #  Pass The Pigs Challenge
# # -----------------------------------------------
import random
p1_score = 0
counter = 0

while p1_score < 100:
    input('Press Enter To Begin')
    pigA = random.randint(1,3)
    pigB = random.randint(1,3)
    print(pigA)
    print(pigB)
    if (pigA == 1 and pigB == 1) or (pigA == 2 and pigB == 2):
        print('==========SIDER.   1 - POINT==========')
        p1_score = p1_score + 1
        counter = counter + 1
        print('Current Score Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif (pigA == 1 and pigB == 2) or (pigA == 2 and pigB == 1):
        print('==========PIG OUT.  BACK TO O POINTS==========')
        p1_score = 0
        counter = counter + 1
        print('Current Score Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif (pigA == 3 and pigB != 3) or (pigA != 3 and pigB == 3) :
        print('==========TROTTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Score Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 3 and pigB == 3:
        print('==========DOUBLE TROTTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Score Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')

print('==========CONGRATULATIONS. IT TOOK YOU',counter,'TURNS==========')
	
# # -----------------------------------------------
# #  Pass the Pigs Challenge Part 2
# # -----------------------------------------------
import random
p1_score = 0
counter = 0

while p1_score < 100:
    input('Press Enter To Begin')
    pigA = random.randint(1,5)
    pigB = random.randint(1,5)
    print(pigA)
    print(pigB)
    if (pigA == 1 and pigB == 1) or (pigA == 2 and pigB == 2):
        print('==========SIDER.   1 - POINT==========')
        p1_score = p1_score + 1
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif (pigA == 1 and pigB == 2) or (pigA == 2 and pigB == 1):
        print('==========PIG OUT.  BACK TO O POINTS==========')
        p1_score = 0
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif (pigA == 3 and pigB != 3) or (pigA != 3 and pigB == 3) :
        print('==========TROTTER.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 3 and pigB == 3:
        print('==========DOUBLE TROTTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 4 or pigB== 4:
        print('==========SNOUTER.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 4 and pigB == 4:
        print('==========DOUBLE SNOUTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 5 or pigB== 5:
        print('==========RAZORBACK.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA == 5 and pigB== 5:
        print('==========DOUBLE RAZORBACK.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
    elif pigA != pigB and pigA + PigB > 7:
        print('==========MISMATCH.  -20 - POINTS==========')
        p1_score = p1_score - 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        print('')
        
print('==========CONGRATULATIONS. IT TOOK YOU',counter,'TURNS==========')

# # -----------------------------------------------
#  Pass The Pigs Challenge Part 3
# -----------------------------------------------
 import random
p1_score = 0
p1_bank = 0
p2_score = 0
p2_bank = 0
counter = 0
p1_over = False
p2_over = False

def player_1():
    global p1_score
    global p1_bank
    global counter
    global p1_over
    input('Press Enter To Begin')
    pigA = random.randint(1,5)
    pigB = random.randint(1,5)
    print(pigA)
    print(pigB)
    p1_over = False
    if (pigA == 1 and pigB == 1) or (pigA == 2 and pigB == 2):
        print('==========SIDER.   1 - POINT==========')
        p1_score = p1_score + 1
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif (pigA == 1 and pigB == 2) or (pigA == 2 and pigB == 1):
        print('==========PIG OUT.  BACK TO O POINTS==========')
        p1_score = 0
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif (pigA == 3 and pigB != 3) or (pigA != 3 and pigB == 3) :
        print('==========TROTTER.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA == 3 and pigB == 3:
        print('==========DOUBLE TROTTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA == 4 or pigB== 4:
        print('==========SNOUTER.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA == 4 and pigB == 4:
        print('==========DOUBLE SNOUTER.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA == 5 or pigB== 5:
        print('==========RAZORBACK.  5 - POINTS==========')
        p1_score = p1_score + 5
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA == 5 and pigB== 5:
        print('==========DOUBLE RAZORBACK.  20 - POINTS==========')
        p1_score = p1_score + 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)
    elif pigA != pigB and pigA + PigB > 7:
        print('==========MISMATCH.  -20 - POINTS==========')
        p1_score = p1_score - 20
        counter = counter + 1
        print('Current Socre Is:', p1_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p1_bank = p1_bank + p1_score
            p1_score = 0
            p1_over = True
            print('Player 1`s BANK:',p1_bank)


def player_2():
    global p2_score
    global p2_bank
    global counter
    global p2_over
    input('Press Enter To Begin')
    pigA = random.randint(1,5)
    pigB = random.randint(1,5)
    print(pigA)
    print(pigB)
    p2_over = False
    if (pigA == 1 and pigB == 1) or (pigA == 2 and pigB == 2):
        print('==========SIDER.   1 - POINT==========')
        p2_score = p2_score + 1
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif (pigA == 1 and pigB == 2) or (pigA == 2 and pigB == 1):
        print('==========PIG OUT.  BACK TO O POINTS==========')
        p2_score = 0
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif (pigA == 3 and pigB != 3) or (pigA != 3 and pigB == 3) :
        print('==========TROTTER.  5 - POINTS==========')
        p2_score = p2_score + 5
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA == 3 and pigB == 3:
        print('==========DOUBLE TROTTER.  20 - POINTS==========')
        p2_score = p2_score + 20
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA == 4 or pigB== 4:
        print('==========SNOUTER.  5 - POINTS==========')
        p2_score = p2_score + 5
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA == 4 and pigB == 4:
        print('==========DOUBLE SNOUTER.  20 - POINTS==========')
        p2_score = p2_score + 20
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA == 5 or pigB== 5:
        print('==========RAZORBACK.  5 - POINTS==========')
        p2_score = p2_score + 5
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA == 5 and pigB== 5:
        print('==========DOUBLE RAZORBACK.  20 - POINTS==========')
        p2_score = p2_score + 20
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)
    elif pigA != pigB and pigA + PigB > 7:
        print('==========MISMATCH.  -20 - POINTS==========')
        p2_score = p2_score - 20
        counter = counter + 1
        print('Current Socre Is:', p2_score)
        print('[[[[[[[[[[[[[[[[[[[[[[NEXT ROUND]]]]]]]]]]]]]]]]]]]]]]')
        opt = input('Do You Want To Bank: 1 - YES  2 - NO')
        if opt == 1:
            p2_bank = p2_bank + p2_score
            p2_score = 0
            p2_over = True
            print('Player 2`s BANK:',p2_bank)


                
while p1_bank < 100 and p2_bank < 100:
    move = random.randint(1,2)
    if move == 1 or p2_over == True:
        print('==========PLAYER 1 IT`S YOUR TURN==========')
        p2_over = False
        print('PLayer 1')
        player_1()
        if p1_bank >= 100:
            print('==========PLAYER 1 YOU WIN==========')
            print('==========CONGRATULATIONS. IT TOOK YOU',counter,'TURNS==========')
    elif move == 2 or p1_over == True:
        print('==========PLAYER 2 IT`S YOUR TURN==========')
        p1_over = False
        print('Player 2')
        player_2()
        if p2_bank >= 100:
            print('==========PLAYER 2 YOU WIN==========')
            print('==========CONGRATULATIONS. IT TOOK YOU',counter,'TURNS==========')
