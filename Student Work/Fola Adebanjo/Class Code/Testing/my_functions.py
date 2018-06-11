# def is_even(number):
# 	if number % 2 == 0:
# 		return True
# 	else:
# 		return False

# def max_of_3(n1, n2, n3):
# 	if (n1> n2) and (n1 > n3):
# 		 return n1
# 	elif (n2 > n1) and (n2 > n3):
# 		 return n2
# 	else:
# 		 return n3#


def upperlower(word):
	""" Returns a count of uppercase and lowercase letters for 
		 a given string. """

	lowercasecount = 0
	uppercasecount = 0

	for letter in word:
		if letter.islower():
			lowercasecount += 1
		elif letter.isupper():
			uppercasecount += 1

	return (lowercasecount, uppercasecount)

print(upperlower("TesTing!"))