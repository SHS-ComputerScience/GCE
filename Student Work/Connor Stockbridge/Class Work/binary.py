#============================================================
#Alfies Version
#============================================================
# def sum(min, max):
# 	a = ((max - min) + 1) * (max + min) / 2
# 	return a

# print(sum(2.5, 11.5))

#============================================================
#My Version
#============================================================
# def sum(min, max):
#     minmax_sum = min + max
#     count = 0
#     for i in range(min, max + 1):
#         count += 1
#     return (minmax_sum * count) / 2

# min = int(input('Enter the starting value:'))
# max = int(input('Enter the maximum value:'))

# print(sum(min, max))
#============================================================
#============================================================
#============================================================



def sum(par1, par2=None):
	# checks for 1 parameter as a list
	if par2 == None and isinstance(par1, list):
		# handle as a list
		total = 0
		for item in list_to_add:
			total = total + item
		return total
	elif par2 != None and not isinstance(par1, list):
		# handle as min and max
		minmax_sum = min + max
		count = 0
		for i in range(min, max + 1):
			count += 1
		return (minmax_sum * count) / 2

# sum of range
# #============================================================
#     minmax_sum = min + max
#     count = 0
#     for i in range(min, max + 1):
#         count += 1
#     return (minmax_sum * count) / 2

# sum of list
#============================================================
# 	total = 0
# 	for item in list_to_add:
# 		total = total + item
# 	return total


test_list = [1.5, 2, 0.5]

sum(10, 50)

"""
sum(1, 10)
sum([1, 2, 3, 4])
#============================================================
name = input('Enter Your Name:')

converted_name = ''

# Converts Name To Binary Representation
for i in range(len(name)):
    den_converted = ord(name[i])
    bin_converted = bin(den_converted)
    binary = (bin_converted[2:] + ' ')
    converted_name += binary
print('Your Name in BInary is:',converted_name)

converted_name = ''

#Converts To Hexadecimal
for i in range(len(name)):
    den_converted = ord(name[i])
    hex_converted = hex(den_converted)
    converted_name += hex_converted
print('Your Name in Hexadecimal is:',converted_name)

converted_name = ''

#Converts To Interger
for i in range(len(name)):
    den_converted = ord(name[i])
    ord_converted = ord(den_converted)
    converted_name += ord_converted
print('Your Name As An Interger is:',converted_name)

"""