# Roman Numeral Converter
def to_roman(number):
	try:
		if number >= 3000: return "Number too big!"
		elif number >= 1000: return "M"  + to_roman(number - 1000)
		elif number >= 900:  return "CM" + to_roman(number - 900)
		elif number >= 500:  return "D"  + to_roman(number - 500)
		elif number >= 400:  return "CD" + to_roman(number - 400)
		elif number >= 100:  return "C"  + to_roman(number - 100)
		elif number >= 90:   return "XC" + to_roman(number - 90)
		elif number >= 50:   return "L"  + to_roman(number - 50)
		elif number >= 40:   return "XL" + to_roman(number - 40)
		elif number >= 10:   return "X"  + to_roman(number - 10)
		elif number >= 9:    return "IX" + to_roman(number - 9)
		elif number >= 5:    return "V"  + to_roman(number - 5)
		elif number >= 4:    return "IV" + to_roman(number - 4)
		elif number >= 1:    return "I"  + to_roman(number - 1)
		else:	return ""
	except TypeError:
		print("ERROR: Invalid input type!")
	except:
		print("ERROR: Unexpected error!")
	return ""