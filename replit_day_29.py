def printColor(color, word):
    if color.lower() == "red":
        print("\033[0;31m" + word + "\033[0m")
    elif color.lower() == "blue":
        print("\033[0;34m" + word + "\033[0m")
    elif color.lower() == "purple":
        print("\033[0;35m" + word + "\033[0m")
    else:
        print("\033[0;32m" + "Green is our best friend!" + "\033[0m")

print("With my", end=" ", sep="")
printColor("purple", "new program")
print("I can just call red to set the color", end=" ")
printColor("red", "and")
print("that word will appear in the color I set it to.", end="\n")
print("")
print("With no", end=" ")
printColor("blue", "weird gaps")
print("")
print("Epic")
