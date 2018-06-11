# def is_even(number):
# 	if number % 2 == 0:
# 		return True
# 	else:
# 		return False

# def sqrt(number):
#     n = 0
#     while True:
#         n_squared = n * n
#         if number == n_squared:
#             return n
#         else:
#             print(n)
#             n += 1
# 		if n_squared >= number:
# 			return None



def string_counter(string):

	lo_counter = 0
	up_counter = 0
	space_counter = 0
	
	for char in string:
		if(char.isupper()):
			up_counter = up_counter + 1
		elif (char.islower()):
			lo_counter = lo_counter + 1
		else:
			space_counter = space_counter + 1
			
	return(up_counter + lo_counter, space_counter)