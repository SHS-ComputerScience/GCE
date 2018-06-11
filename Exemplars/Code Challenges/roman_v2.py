# Roman Numeral Converter v2

ARABIC = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMAN = "M CM D CD C XC L XL X IX V IV I".split()

def to_roman(integer):
	numerals = []
	for arabic, roman in zip(ARABIC, ROMAN):
		numeral, integer = divmod(integer,arabic)
		numerals.append(roman * numeral)
	return ''.join(numerals)
