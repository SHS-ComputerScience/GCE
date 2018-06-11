# -----------------------------------------------
#  Text Dice Challenge
# -----------------------------------------------
import random
index = random.randint(1, 6)
words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
print(words.pop(index - 1))
# -----------------------------------------------
#  Text Dice Challenge
# -----------------------------------------------
n0 = []
n1 = []
n2 = []
n3 = []
n4 = []
n5 = []
n6 = []
n7 = []
n8 = []
n9 = []

print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)

selection = input('Choose your list 1 to 10: ')
if selection == '1':
    note_to_store = input('What do you wish to store: ')
    del n0[:]
    n0.append(note_to_store)
    print(n0)
elif selection == '2':
    note_to_store = input('What do you wish to store: ')
    del n1[:]
    n1.append(note_to_store)
    print(n1)
