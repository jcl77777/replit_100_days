loan = 1000
interestRate = 0.05

for i in range (10):
  loan +=  loan * interestRate
  print("Year", i+1, "is", round(loan,2))