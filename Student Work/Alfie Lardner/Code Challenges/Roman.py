def get_roman(number):

	UNITS     = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
	TENS      = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
	HUNDREDS  = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
	THOUSANDS = ("", "M")

	ten, unit = divmod(number, 10)
	thousand, hundred = divmod(number, 1000)

	if number < 100:
		return number, TENS[ten] + UNITS[unit]
	elif number < 1000:
		ten %= 10
		hundred %= 10
		thousand %= 10
		return number, THOUSANDS[thousand] + HUNDREDS[hundred] + TENS[ten] + UNITS[unit]

# test = [get_roman(x) for x in range(1, 100)]
# print(test)



