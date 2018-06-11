# """
# ===============================================
#  PROGRAMMING COMPANION OBJECTIVE 08 
# ===============================================

# KEY LEARNING POINTS:
#  - Subroutines, procedures and functions
 
# KEY WORDS:
#  - def
#  - global
#  - return
 
# """

# -----------------------------------------------
#  VAT Challenge
# -----------------------------------------------

# def get_vat(price):
# 	return price * 0.2

# item_price = float(input("Enter price of item: "))
# vat = get_vat(item_price)

# print("VAT = £%.2f" % vat)

# -----------------------------------------------
#  Conversion Challenge
# -----------------------------------------------

# def get_imperial():
# 	if input1 == ("millimetre"):
# 		input("How many millimetres?:")
# 		print(input1*0.0394)
# 	if input1 == ("centimetre"):
# 		input("How many centimetre?")
# 		print(input1*0.3937 )
# 	if input1 == ("decimetre"):
# 		input("How many decimetres ?")
# 		print(input1*3.937)
# 	if input1 == ("metre"):
# 		input("How many metres ?")
# 		print(input1*1.0936)
# 	if input1 == ("tonne"):
# 		input("How many tonnes ?")
# 		print(input1*0.984)
# 	if input1 == ("kilometre"):
# 		input("How many kilometres ?")
# 		print(input1*0.6214)
# 	if input1 == ("millilitre"):
# 		input("How many millilitres ?")
# 		print(input1 *0.002)
# 	if input1 == ("litre"):
# 		input("How many litres ?")
# 		print(input1*1.76)
# 	if input1 == ("gram"):
# 		input("How many grams?")
# 		print(input1*15.43)
# 	if input1 == ("kilogram"):
# 		input("How many kilograms ?")
# 		print(input1*2.205)

# input1 = input("Enter Name of Imperial").lower()
# metric = get_imperial(input1)



# -----------------------------------------------
#  Conversion Challenge 2
# -----------------------------------------------



# -----------------------------------------------
#  Darts Challenge
# -----------------------------------------------

# score = 501
# while score > 0:
# 	scored = int(input("Total of round: "))
# 	score -= scored
# 	print ("Current score =", score)
# 	if score == 0:
# 		print("WINNER!")
# 	if score < 0:
# 		score = 501
# 		print("Start Again")
# -----------------------------------------------
#  Darts Challenge 2
# -----------------------------------------------

# p1_score = 501
# p2_score = 501
# count = 0

# while p1_score > 0 or p2_score > 0:
# 	count +=1
# 	p1_scored = int(input("PLAYER 1 - Total of round: "))
# 	p1_score -= p1_scored
# 	print ("PLAYER 1 - Current score =", p1_score)
# 	p2_scored = int(input("PLAYER 2 - Total of round: "))
# 	p2_score -= p2_scored
# 	print ("PLAYER 2 - Current score =", p2_score)
# 	print("Round", count, "Complete")
# 	if p1_score == 0:
# 		print("PLAYER 1 IS THE WINNER!")
# 		break
# 	if p2_score == 0:
# 		print("PLAYER 2 IS THE WINNER!")
# 		break
		
# -----------------------------------------------
#  Snake Eyes Challenge
# -------------------------------------------

# import random

# total_score = 0
# banked_total = 0
# gamble = 0


# p1roll = print(random.randint(1,6))
# p1roll2 = print(random.randint(1,6))
# total_score = p1roll + p1roll2
# if p1roll == 1 != p1roll2 == 1:
#     total_score = 0
# if p1roll == 1 and p1roll2 == 1:
#     total_score = 0
#     banked_total = 0
# elif p1roll not == 1 or p1roll2 not == 1:
#     g_or_b = input("Gamble or Bank?")
#     if g_or_b == "Gamble":
#         total_score = p1roll + p1roll2
#     if g_or_b == "Bank":
#         banked_total = p1roll + p1roll2
#         total_score = 0
        
        


# p2roll = print(random.randint(1,6))
# p2roll2 = print(random.randint(1,6))
# total_score = p1roll + p1roll2


	
# -----------------------------------------------
#  Pass the Pigs Challenge
# -----------------------------------------------
 
	
# -----------------------------------------------
#  Pass the Pigs Challenge 2
# -----------------------------------------------



# -----------------------------------------------
#  Pass the Pigs Challenge 3
# -----------------------------------------------
 
