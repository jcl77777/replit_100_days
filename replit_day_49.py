'''
🌟Current Leader🌟

Analyzing high scores......

Current leader is DJM 898,000
'''
import time

print("🌟Current Leader🌟")
print("Analyzing high scores......")
time.sleep(2)

f = open("high.score", "r")
contents = f.read().split("\n")
f.close()

max_score = 0
name = None

for i in contents:
  numbers = i.split()
  if numbers != []:
    if int(numbers[1]) > max_score:
      max_score = int(numbers[1])
      name = numbers[0]

print(f"Current leader is {name} with {max_score}")
