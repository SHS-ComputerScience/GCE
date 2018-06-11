name = "Billahalla"
b_name = ""
h_name = ""
d_name = ""

for letter in name:
	denary = ord(letter)
	d_name += str(denary)
	binary = bin(denary)
	b_name += binary
	hexadecimal = hex(denary)
	h_name += hexadecimal

print(d_name)
print(b_name)
print(h_name)
