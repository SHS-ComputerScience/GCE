def sum(par1, par2=None):
	# checks for 1 parameter as a list
	if par2 == None and isinstance(par1, list):
		# handle as a list
	elif par2 != None and not isinstance(par1, list):
		# handle as min and max
		
# sum of range
#     minmax_sum = min + max
#     count = 0
#     for i in range(min, max + 1):
#         count += 1
#     return (minmax_sum * count) / 2		
		
# sum of list	
# 	total = 0
# 	for item in list_to_add:
# 		total = total + item
# 	return total

test_list = [1.5, 2, 0.5]

sum(10, [50])

"""
sum(1, 10)
sum([1, 2, 3, 4])

"""

#I have no idea