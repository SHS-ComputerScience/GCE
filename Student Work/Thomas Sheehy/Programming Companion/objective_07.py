#------------------------------
#        XP Challenge
#------------------------------

# totalxp = 2001
# rank = 1

# while totalxp > 2000:
# #     XP = int(input("How much XP did you earn last game?"))
#     xp = 800
#     new_totalxp = xp + totalxp
#     if new_totalxp >= 2000:
#         print("You have been promoted!")
#         new_totalxp2 = 0 + (totalxp - 2000)
#         new_rank = rank + 1
#         print (new_totalxp2, new_rank)
#     else:
#         print (totalxp, rank)
# new_rank = rank
# new_totalxp = totalxp

# xp = 0
# rank = 1
# # while xp < xp:
# # while xp < 2000:
# xp_earned = xp_earned + int(input("How much XP did you earn last game?"))
# # xp_earned = 550
# # xp = xp_earned + xp
# if xp >= 1500:
# 	print ("You have been promoted to Warrent Officer")
# 	print ("Your XP is", xp, "and your rank is", rank)
# 	rank = rank + 4
# 	xp = xp_earned - 1500
# elif xp >= 700:
# 	print ("You have been promoted to Staff Sergeant")
# 	print ("Your XP is", xp, "and your rank is", rank)
# 	rank = rank + 3
# 	xp = xp_earned - 700
# elif xp >= 300:
# 	print ("You have been promoted to Sergeant")
# 	print ("Your XP is", xp, "and your rank is", rank)
# 	rank = rank + 2
# 	xp = xp_earned - 300
# elif xp >= 100:
# 	print ("You have been promoted to Corporal")
# 	print ("Your XP is", xp, "and your rank is", rank)
# 	rank = rank + 1
# 	xp = xp_earned - 100
# elif xp <= 100:
# 	print ("Your XP is", xp, "and your rank is", rank)
# 	xp = xp_earned + xp
# else:
# 	print ("Maximum rank achieved.")

XP = 0
Player_rank = 1

while XP < 2000:
#XP = XP + int(input('How much XP did you earn last game:'))
	XP = 550
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