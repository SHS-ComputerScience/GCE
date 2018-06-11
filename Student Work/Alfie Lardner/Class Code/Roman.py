def toRoman(n):
	if n<1 or n > 39:
		return 'Invalid'

	result = ""
	while n > 0:
		if n >= 10:
			result += 'X'
			n =- 10

		elif n == 9:
			result += 'IX'
			n -= 9
		elif n >= 5:
			result + 'V'
			n -= 5
		elif n == 4:
			result += "IV"
			n -= 4

		else:
			result += 'I'
			n -= 1

	return result

print([(i,toRoman(i)) for i in range(40)])




