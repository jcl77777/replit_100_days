def printColor(color):
    if color == "red":
        return("\033[0;31m")
    elif color == "blue":
        return("\033[0;34m")
    elif color == "purple":
        return("\033[0;35m")
    elif color == "green":
        return("\033[0;32m")
    elif color == "yellow":
        return("\033[0;33m")
    elif color == "white":
        return("\033[0;37m")
    else: 
      return("\033[0m")


title = f"{printColor('red')}={printColor('white')}={printColor('blue')}={printColor('white')} Music App {printColor('blue')}={printColor('white')}={printColor('red')}="

print(f"{title:^35}")
print(f"🔥▶️\t{printColor('white')}Radio Gaga")
print(f"{printColor('yellow')}Q️ueen")

print("\033[0m" + "PREV", "\033[0;32m" + "NEXT", "\033[0;35m" + "PAUSE", sep="\v")

print("")
text = "WELCOME TO"
print(f"{printColor('default')}{text:^35}")
text = "--    ARMBOOK   --"
print(f"{printColor('blue')}{text:^35}")
text = "Definitely not a rip off of "
print(f"{printColor('yellow')}{text:>35}")
text = "a certain other "
print(f"{printColor('yellow')}{text:>35}")
text = "social networking site."
print(f"{printColor('yellow')}{text:>35}")
text ="Honest"
print(f"{printColor('red')}{text:^35}")
print("")
text = "Username: "
username = input((f"{printColor('white')}{text:^35}"))
text = "Password: "
password = input((f"{printColor('white')}{text:^35}"))