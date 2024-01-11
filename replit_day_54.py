'''
🌟Shop $$ Tracker🌟

Your shop took £592 pounds today.
'''

import csv

print("🌟Shop $$ Tracker🌟")

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)

  total = 0 
  for row in reader:
    sum = float(row["Cost"]) * float(row["Quantity"])
    total +=float(sum)
    print(f"Total: S{round(total,2)} today.")