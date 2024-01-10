'''
🌟Dave's Dodgy Pizzas🌟

How many pizzas? > three
You must input a numerical character, try again. > 3

What size? > XXXXXX

Name please > David

Thanks David, your pizzas will cost XXXXX
'''
customer_order =[]

print("🌟Dave's Dodgy Pizzas🌟")

try:
  f = open("order.txt","r")
  customer_order = eval(f.read())
except Exception:
  print("ERROR: Unable to load")
  
while True:
  try:
    amount = int(input("How many pizza?> "))
    size = input("What size? (L/S)> ")
    if size.lower() == "l":
      cost = amount*300
    elif size.lower() == "s":
      cost = amount*100
    else: 
      print("Invalid input. Please enter L or S.")
      continue
  
  except Exception as err:
    print("You must input a numerical character, try again. > ")
    print(err)
    continue
  
  name = input("Name please> ")
  print(f"Thanks {name}, your pizzas will cost {cost}")

  # Add the current order to the list
  customer_order.append({"Name": name, "Amount": amount, "Size": size, "Cost": cost})

  # Ask if the user wants to place another order
  another_order = input("Place another order? (yes/no) > ").lower()
  if another_order != "yes":
    break

try:
  f = open("order.txt", "w") 
  f.write(str(customer_order)) 
  f.close()
except Exception as e:
  print(f"ERROR: Unable to load {e}")