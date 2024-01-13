'''
🌟Factorial Finder🌟

Input a number > 5

The factorial of 5 is 120.
'''
def factorial(n):
  if n <= 0:
    return 1
  else:
      return n*factorial(n-1) 

print("🌟Factorial Finder🌟")

num = int(input("Input a number > "))
result = factorial(num)

print(f"The factorial of {num} is: {result}")