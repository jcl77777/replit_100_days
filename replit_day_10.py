myBill = float(input("What was the bill?: "))
tip = float(input("What percentage would you like to tip?: "))
total = float(myBill*(1+tip/100))

numberOfPeople = int(input("How many people?: "))
split = total / numberOfPeople
finalAmount = round(split , 5)
print("You all owe", finalAmount)
