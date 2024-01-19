import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("300x300") 

answer = 0
lastNumber = 0
operator = None

#return value
def ans(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer 

#return last number, answer and operator
def calcAns(Op):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if Op == "+":
    operator = "+"
  elif Op == "-":
    operator = "-"
  elif Op == "*":
    operator = "*"
  elif Op == "/":
    operator = "/"
  hello["text"] = answer

#return calculation with last number and operator
def calc():
  global answer, lastNumber, operator
  print(f"{lastNumber}\t{answer}\t{operator}")
  if operator == "+":
    total = lastNumber + answer
  elif operator == "-":
    total = lastNumber - answer
  elif operator == "*":
    total = lastNumber * answer
  elif operator =="/":
    total = lastNumber / answer
  answer = total
  hello["text"] = answer


hello = tk.Label(text = answer)
hello.grid(row=0, column=1)

#row1
button = tk.Button(text = "1", command = lambda: ans(1)).grid(row=1, column=0)

button = tk.Button(text = "2", command = lambda: ans(2)).grid(row=1, column=1)

button = tk.Button(text = "3", command = lambda: ans(3)).grid(row=1, column=2)

button = tk.Button(text = "+", command = lambda: calcAns("+")).grid(row=1, column=3)

button = tk.Button(text = "-", command = lambda: calcAns("-")).grid(row=1, column=4)

#row 2
button = tk.Button(text = "4", command = lambda: ans(4)).grid(row=2, column=0)

button = tk.Button(text = "5", command =lambda: ans(5)).grid(row=2, column=1)

button = tk.Button(text = "6", command =lambda: ans(6)).grid(row=2, column=2)

button = tk.Button(text = "*", command = lambda: calcAns("*")).grid(row=2, column=3)

button = tk.Button(text = "/", command = lambda: calcAns("/")).grid(row=2, column=4)

#row 3
button = tk.Button(text = "7", command = lambda: ans(7)).grid(row=3, column=0)

button = tk.Button(text = "8", command = lambda: ans(8)).grid(row=3, column=1)
button = tk.Button(text = "9", command = lambda: ans(9)).grid(row=3, column=2)

#row 4
button = tk.Button(text = "0", command =lambda: ans(0)).grid(row=4, column=1)
button = tk.Button(text = "=", command = calc).grid(row=4, column=3)


tk.mainloop()