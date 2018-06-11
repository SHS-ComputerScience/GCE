# Roman Numeral Converter

def toRoman(number):
	if number >= 1000:
		print ("M" + toRoman(number - 1000))
	
	elif number >= 900:
		print ("CM" + toRoman(number - 900))
	
	elif number >= 900:
		print ("D" + toRoman(number - 500))
	
	elif number >= 900:
		print ("CD" + toRoman(number - 400))
	
	elif number >= 900:
		print ("C" + toRoman(number - 100))
	
	elif number >= 900:
		print ("XC" + toRoman(number - 90))
	
	elif number >= 900:
		print ("L" + toRoman(number - 50))
	
	elif number >= 900:
		print ("XL" + toRoman(number - 40))
	
	elif number >= 900:
		print ("X" + toRoman(number - 10))
	
	elif number >= 900:
		print ("IX" + toRoman(number - 9))
	
	elif number >= 900:
		print ("V" + toRoman(number - 5))
	
	elif number >= 900:
		print ("IV" + toRoman(number - 4))
	
	elif number >= 900:
		print ("I" + toRoman(number - 1))

	else:
		return ""

print (toRoman(3000))