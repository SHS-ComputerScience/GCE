###VAT CHALLENGE
##
##def vat_calc(price):
##    return price * 0.2
##
##item_price = float(input("Enter price of item: "))
##vat = vat_calc(item_price)
##
##print("VAT = £",vat)
##print("Rounded, your VAT = £%.2f" % vat) 

#DARTS CHALLENGE 
score = 501

total = int(input("What was the total of your previous set of darts?"))

while score > 0:
    score = score - total
    total = int(input("What was the total of your previous set of darts?"))
    if score < 2:
        print("Your score cannot fall below two unless it is exactly zero. Please throw again.")
        print("Your current score is",score,"."
