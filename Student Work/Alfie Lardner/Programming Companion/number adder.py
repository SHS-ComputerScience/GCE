

def sum(min, max):
	a = ((max - min) + 1) * (max + min) / 2
	return a

min = int(input("Enter an integer: "))
max = int(input("Enter a second integer greater than the first integer: "))

print("all numbers from your first number to your second number adds up to:",sum(min, max))