#-----------------
#Objective 2
#-----------------

#Tasks

#1
#Inputting strings into python
print("Hello")
name_entered = input("What is ur name?")
print("Thank You", name_entered)

#2
year = int(input("What year is it please?"))
print("Ah, it is", year,"thank you.")

#3
print("Hiya what's ur name?")
user_name = input()
print("How old r u?")
user_age = input()
print("Thank you", user_name,",Ur registered age is", user_age)

#Challenges

#Simple adder challenge
print("Enter the first number")
num_1 = int(input())

print("Enter the second number")
num_2 = int(input())

Sum = num_1 + num_2

print("first number added to the second gives u", Sum)

#Test marks challenge
print("Enetr three test marks out of 100")

mark_1 = int(input())
mark_2 = int(input())
mark_3 = int(input())

average = mark_1 + mark_2 + mark_3 / 3

print("Ur average =", average)

#Temperature converter challenge
print("Input tempreture in fahrenheit")

f_temp = float(input())
c_temp = (f_temp - 32)* (5/9)

print(f_temp,"fahrenheit in centigrade is", c_temp)

#Height and weight challenge
print("Input ur height in inches")
i_height = float(input())
c_height = float(2.54 * i_height)

print("Input ur weight instones")
s_weight = float(input())
k_weight = float(6.364 * s_weight)

print("Ur height in cm is", c_height, "and ur weight in kg is", k_weight)

#Toy car challenge
print("Input the number of hours worked")
hour = float(input())
n_wage = float(hour * 9)   
print("Input the number of toy cars made")
cars = float(input())      
c_wage = float(cars * 0.60)

day_wage = n_wage + c_wage

print("Ur total wage for the day is", day_wage)      

#Fish tank volume challenge
l_tank = float(input("Input length of the fish tank"))
d_tank = float(input("Input depth of the fish tank"))
h_tank = float(input("Input height of the fish tank"))

volume = float(l_tank * d_tank * h_tank / 1000)

print("The volume of water needed is", volume)                

#Circle properties challenge

diameter = float(input("Input the diameter of the circle"))
radius = float(diameter / 2)
print("Radius =", radius)

area = float(radius * radius * 3.14)
print("Area =", area)

circumference = float(2 * 3.14 * radius)
print("circumference =", circumference)

arc_angle = float(input("Input the arc angle of the circle"))                 
arc_length = float(circumference * arc_angle / 360)
print("Arc length =", arc_length)

