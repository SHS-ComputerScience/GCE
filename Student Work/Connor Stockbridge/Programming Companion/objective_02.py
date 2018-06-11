#                   Objective 2 - Connor Stockbridge - 11/09/2017
#                                       Task 1
#                               Inputting strings in Python
print("Hello")
name_entered = input("What is your name? ")
print("Thank you",name_entered)

#                                       Task 2
year = int(input("What year is it please? "))
print("Ah, it is",year,"thank you.")

#                                       Task 3
print('Hello')
PersonsName = input('And your name is? ')
print('Oh, Hello',PersonsName)
PersonsAge = input('And how old are you? ')
print('So your',PersonsAge)

#                                Simple Adder Challenge
FirstNumber = int(input('What is your fist number?'))
SecondNumber = int(input('What is youyr second number?'))
print(FirstNumber + SecondNumber)

#                                 Test Marks Challenge  
FirstScore = int(input('What was the first test score?'))
SecondScore = int(input('What was the second test score?'))
ThirdScore = int(input('What was the final test score?'))
TotalScore = FirstScore + SecondScore + ThirdScore
print(TotalScore/3)

#                           Temperature Converter Challenge
FahrenTemp = float(input('What is todays Fahrenheit Temperature? '))
CentiTemp = (FahrenTemp - 32)*(5/9)
print(CentiTemp)

#                           Height And Weight Challenge
HeightInch = float(input('What is your height measured in inches? '))
WeightStone = float(input('What is your weight measured in stone? '))
CentiHeight = (HeightInch*2.54)
KiloWeight = (WeightStone*6.364)
print('Did you know your height is',CentiHeight,'cm, and your weight is',KiloWeight,'Kg.')

#                                   Toy Car Challenge
WorkHours = float(input('How long did you work for today?'))
ProductionBonus = int(input('How many toy cars did you make today?'))
WorkWage = (WorkHours*9)
BonusWage = (ProductionBonus*0.60)
FinalWage = (WorkWage + BonusWage)
print(FinalWage)

#                               Fish Tank Volume Challenge
TankLength = float(input('What is the length of the fish tnk in cm?'))
TankDepth = float(input('What is the depth of the fish tank measured in cm?'))
TankHeight = float(input('What is the height of the fish tank in cm?'))
LitresRequired = (TankLength*TankDepth*TankHeight)/1000
print('You will need',LitresRequired,'Litres to fill your fish tank.')

#                               Circle Propertities Challenge
Diameter = int(input('What is the diameter of this circle?'))
Radius = (Diameter/2)
print(Radius)
print(Radius*3.14)
Circumfrence = (Diameter*3.14)
print(Circumfrence)
Arc = int(input('What is the length of the arc angle?'))
ArcLength = (Circumfrence*Arc)/360
print(ArcLength)