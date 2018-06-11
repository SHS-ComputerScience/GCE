##
###Square Numbers Challenge 
##
##for counter in range(1, 21):
##    square = counter * counter
##    print(counter, "squared is", square)
##


### 9 Green Bottles Challenge
##bottles = int(input("Enter a number between 1-10"))
##
##if bottles == 10:
## print("10 green bottles sitting on the wall")
## print("9 green bottles sitting on the wall")
## print("8 green bottles sitting on the wall")
## print("7 green bottles sitting on the wall")
## print("6 green bottles sitting on the wall")
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
## 
##if bottles == 9:
## print("9 green bottles sitting on the wall")
## print("8 green bottles sitting on the wall")
## print("7 green bottles sitting on the wall")
## print("6 green bottles sitting on the wall")
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 8:
## print("8 green bottles sitting on the wall")
## print("7 green bottles sitting on the wall")
## print("6 green bottles sitting on the wall")
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 7:
## print("7 green bottles sitting on the wall")
## print("6 green bottles sitting on the wall")
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 6:
## print("6 green bottles sitting on the wall")
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 5:
## print("5 green bottles sitting on the wall")
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 4:
## print("4 green bottles sitting on the wall")
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 3:
## print("3 green bottles sitting on the wall")
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 2:
## print("2 green bottles sitting on the wall")
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##
##if bottles == 1:
## print("1 green bottles sitting on the wall")
## print("No green bottles sitting on the wall")
##


#Times Table Challenge



##
###ROT13
##
##
##plain_text = input("Enter plain text: ")
##
##for i in range(len(plaintext)):
##    ord(plaintext[i])
##    ordinal_value = ord(letter)
##    shifted_value = ordinal_value + 13
##    shifted_char = chr(shifted_value)
##    cipher = cipher + shifted_char
##    
##    cipher += ord(letter) + 13 
##            
##print(cipher)




###LETTER GAME CHALLENGE
##
##
##letters1 = "EARIOTNSLCUDP"
##letters2 = "MHGBFYWKVXZJQ"
##scoresHx = "123456789ABCD"
##score = 0
##
##word = input("Please enter a word.").upper()
##
##for char in word:
##  index = letters1.find(char)
##  if index == -1:
##     index = letters2.find(char)
##     value = int(scoresHx[index], 16) + 13
##  else:
##    value = int(scoresHx[index], 16)
##  score = score + value
## 
##print(score)