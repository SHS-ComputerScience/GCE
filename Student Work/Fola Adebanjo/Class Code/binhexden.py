# My one:

# # def all_name():
# 	name = input("first name: ")
# 	for letter in name:
# 		den = (ord(letter))
# 		print(letter,":", den)
# 		print(letter,":", bin(den))
# 		print(letter,":", hex(den))

# all_name()


# Tom's:

# word = input("Input a word to be converted to binary, oct and hex:")
# type_list = [bin, oct, hex]
# for i in type_list:
# 	for letter in word:
# 		print(i(ord(letter)))


name = "Please enter your name."
converted_name = "" 

for i in range(len(name)):
	denary = ord(name[i])
	binary = bin(denary)
	converted_name += binary

converted_name += "\n\n"

for i in range(len(name)):
	denary = ord(name[i])
	hexadecimal = hex(denary)
	converted_name += hexadecimal

converted_name += "\n\n"

for i in range(len(name)):
	denary = ord(name[i])
	converted_name += str(denary)

print("Your name converted is", converted_name, ".")
