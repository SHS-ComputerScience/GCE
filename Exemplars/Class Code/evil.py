# evil numbers

number = 1023

def is_evil(n):
	temp = True
	while n > 0:
		if n % 2 == 1:
			temp = not temp
			n -= 1
		n = n // 2
	return temp

print( is_evil(number) )
if is_evil(number):
	print(bin(number))