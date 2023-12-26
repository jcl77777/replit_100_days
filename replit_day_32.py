import random

#solution1
helloLanguage = ["Hello", "Hola", "Bonjour", "Hallo", "Ciao", "Ni hao", "Konnichiwa", "Ola", "Aloha", "Guten Tag"]
language = helloLanguage[random.randint(0, len(helloLanguage) - 1)]
print(f"{language}")

#solution2
greetings = ["Hello", "Hola", "Bonjour", "Hallo", "Ciao", "Ni hao", "Konnichiwa", "Ola", "Aloha", "Guten Tag"]
index = random.randint(0,9)
print(f"{greetings[index]}")