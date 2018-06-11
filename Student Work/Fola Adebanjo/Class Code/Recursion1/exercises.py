# # ------------------------------------------------------------
# # Recursive Function Example:
# # ------------------------------------------------------------

# def reverse_str_recursive(string):
# 	""" Returns a reversed string of string."""
# 	string = str(string)
# 	if string == '':
# 		return string
# 	else:
# 		return reverse_str_recursive(string[1:]) + string[0]

# # ------------------------------------------------------------
# # Recursion Exercise 1:
# #   Write a function to calculate the sum of a list of
# #   numbers.
# # ------------------------------------------------------------

# def list_sum(n_list):
# 	""" Returns the sum of a list of numbers."""
# 	if n_list == 0:
# 		return 0  # End of recursion #
# 	else:
# 		return n_list[0] + list_sum(n_list[1:]) # Recursion #

# # ------------------------------------------------------------
# # Recursion Exercise 2:
# #   Write a function to get the factorial of a non-negative
# #   integer.
# # ------------------------------------------------------------

# def factorial(n):
# 	""" Returns the factorial of a non-negative integer."""
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)

# # ------------------------------------------------------------
# # Recursion Exercise 3:
# #   Write a function to solve the Fibonacci sequence.
# # ------------------------------------------------------------

# def fibonacci(n):
# 	""" Return solved Fibonacci sequence."""
# 	if n == 2 or n == 1:
# 		return 1
# 	elif n == 0 or n = float:
# 		return
# 	else:
# 		return + fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))

# # ------------------------------------------------------------
# # Recursion Exercise 4:
# #   Write a function to calculate the sum of an n-dimensional
# #   list of numbers.
# # ------------------------------------------------------------

# def n_dimensional_list_sum(n_list):
# 	""" Return the sum of an n-dimensional list of numbers."""
# 	#declare cumalative total variable
# 	total = 0
		
# 	For i=0 to nLlist.length - 1 
# 		if Nlist = llist Then 
# 			return total + nDimensionalListSum(nList[i])
# 		else
# 			total = total +nList[i]
# 		end if 
# 	next i 
# 	return total
# end function

# # ------------------------------------------------------------
# # Recursion Exercise 5:
# #   Write a function to converting an Integer to a string in
# #   any base.
# # ------------------------------------------------------------

def toStr(n, base):
	""" Returns string of integer in given base."""
	convertstring = "0123456789ABCDEF"
	if n < base:
		return convertstring[n]
	else:
		return toStr(n//base, base)

