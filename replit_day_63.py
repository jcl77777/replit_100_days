import random

num = random.randint(10,100)

def countdown():
  for i in range(num):
    print(i+1)

#import test's function to be used in main.py
import test as tt

print("Countdown")
tt.countdown()