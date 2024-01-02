import random

values = []

for i in range(8):
    number = random.randint(0, 90)
    # numbers not repeated
    if number in values:
        continue
    # numbers added to the list
    else:
        values.append(number)

# numbers sorted
values.sort()

# Create a bingo list with three sublists
bingo_list = [
    [values[0], values[1], values[2]],
    [values[3], "BINGO", values[4]],
    [values[5], values[6], values[7]]
]

# Print each row
for row in bingo_list:
    print(row)