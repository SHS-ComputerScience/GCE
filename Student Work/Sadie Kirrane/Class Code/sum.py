def sum(firstNumber, secondNumber=None):
	# checks for 1 parameter as a list
	if secondNumber == None and isinstance(firstNumber, list):
		#The major flaw here is counting between two floats.  As the floats could be infinite
		#Also could exhaust memory so should be restricted to a specific precision
		#
		# handle as a list
		total = 0
		for item in firstNumber:
			total = total + item
		return total

	elif secondNumber != None and not isinstance(firstNumber, list):
		#Is the first or second param actually a float?
		#If so we need to convert to a list and then recursviely call this function
		if isinstance(firstNumber,float) or isinstance(secondNumber,float):
			inputFloats = '{0:2f}, {1:2f}'.format(firstNumber, secondNumber)
			myNewList = map(float, inputFloats.split(','))
			return sum(list(myNewList))

		# handle as min and max
		total = firstNumber + secondNumber
		count = 0

		for i in range(firstNumber, secondNumber + 1):
			count += 1
		return (total * count) / 2


print(sum([1.01,1.05]))

print(sum(1.01, 1.05))

print(sum(1, 10))