word = input("Input a word to be converted to binary, oct and hex:")
type_list = [bin, oct, hex]
for i in type_list:
	for letter in word:
		print(i(ord(letter)))