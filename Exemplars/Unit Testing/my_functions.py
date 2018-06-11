# --------------------------------------------------------------------
# uppercase and lowercase letter counter
# --------------------------------------------------------------------

def isupper(char):
	return True if ord(char) >= 65 and ord(char) <= 90 else False

def islower(char):
	return True if ord(char) >= 97 and ord(char) <= 122 else False

def count_upper_lower_iterative(string):
	upper_count = 0
	lower_count = 0
	for char in string:
		upper_count += isupper(char)
		lower_count += islower(char)
	return (upper_count, lower_count)

def count_upper_lower_recursive(string):
	return (0, 0) if string == '' else (isupper(string[0]) + count_upper_lower_recursive(string[1:])[0],
													islower(string[0]) + count_upper_lower_recursive(string[1:])[1])

# --------------------------------------------------------------------
# string reversal
# --------------------------------------------------------------------

def reverse_str_short(string):
	return str(string)[::-1]

def reverse_str_long(string):
	reversed_str = ''
	count = 1
	for i in range(0, len(str(string))):
		reversed_str += string[len(string) - count]
		count += 1
	return reversed_str

def reverse_str_recursive(string):
	string = str(string)
	if string == '':
		return string
	else:
		return reverse_str_recursive(string[1:]) + string[0]

# --------------------------------------------------------------------
# highest of three values
# --------------------------------------------------------------------

def max_of_3(n1, n2, n3):
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n1 and n2 > n3:
		return n2
	else:
		return n3

# --------------------------------------------------------------------
# even number tester
# --------------------------------------------------------------------

def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

# --------------------------------------------------------------------
# square root calculator
# --------------------------------------------------------------------

def sqrt(number):
	n = 0
	while True:
		nsquared = n * n
		if number == nsquared:
			return n
		else:
			n += 1
		if nsquared >= number:
			return None
