def sum(par1, par2=None):
	# checks for 1 parameter as a list
	if par2 == None and isinstance(par1, list):
		# handle as a list
		total = 0
		for item in par1:
			total = total + item
		return total
	elif par2 != None and not isinstance(par1, list):
		# handle as min and max
		sum = par1 + par2
		count = 0
		for i in range(par1, par2 + 1):
			count += 1
		return (sum * count) / 2

test_list = [1.5, 2, 0.5]

print(sum(1, 10))
print(sum([1, 2, 3, 4]))