"""
Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
"""
import os, time
listOfEmail = []

#print email overview
def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 0
  for index in range(len(listOfEmail)): 
    print(f"{index}: {listOfEmail[index]}") 
    counter += 1 
  time.sleep(1)

#spam letter to each input email
def spam():
  letter = "  It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway."
  finalWords = "Love and hugs,"
  name = "Ian Spammington III"
  for index in range(len(listOfEmail)):
    print(f"Dear {listOfEmail[index]},\n{letter}\n{finalWords}\n{name}")
    
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    if email not in listOfEmail:
      listOfEmail.append(email)
    #store only one time:
    elif email in listOfEmail:
      print(f"{email} is already in the list")
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    elif email not in listOfEmail:
      print(f"{email} not found")
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    #return no email
    if len(listOfEmail) == 0:
      print("No emails to spam")
    else:
      spam()
      time.sleep(5)
  time.sleep(1)
  os.system("clear")