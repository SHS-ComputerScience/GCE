name = input("Please enter your name.")
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