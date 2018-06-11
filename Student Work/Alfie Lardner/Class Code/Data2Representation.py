name = input("Enter your name: ")
name_converted = ""
print("")
print("1) Binary")
print("2) Hexadecimal")
print("3) Denary")
print("")

choice = int(input("Enter the number of your chosen conversion: "))

if choice == 1:
	for i in range(len(name)):
		denary = ord(name[i])
		binary = bin(denary)
		name_converted += binary

	name_converted += "\n\n"

elif choice == 2:
	for i in range(len(name)):
		denary = ord(name[i])
		hexadecimal = hex(denary)
		name_converted += hexadecimal

	name_converted += "\n\n"

elif choice == 3:
	for i in range(len(name)):
		denary = ord(name[i])
		name_converted += str(denary)

print("Your name converted is", name_converted)
