# Objective 07
# XP Challenge

xp_total = 0
rank = 1

while rank < 5:
	xp_earned = int(input("Enter previous XP: "))
	xp_total = xp_total + xp_earned
	if xp_total >= 1500:
		print("You have been promoted!")
		xp_carried_over = xp_total - 100
		xp_total = 0
		rank = rank + 1
	elif xp_total >= 700:
		print("You have been promoted!")
		xp_carried_over = xp_total - 100
		xp_total = 0
		rank = rank + 3
	elif xp_total >= 300:
		print("You have been promoted!")
		xp_carried_over = xp_total - 100
		xp_total = 0
		rank = rank + 1
	elif xp_total >= 100:
		print("You have been promoted!")
		xp_carried_over = xp_total - 100
		xp_total = 0
		rank = rank + 1
	else: