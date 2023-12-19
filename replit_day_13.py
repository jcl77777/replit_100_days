print("Exam Grade Calculator")
print()
testName = input("What is the name of the test? ")
maxScore = int(input("What is the max score in " + testName + "? "))
testScore = int(input("What is your score in " + testName + "? "))
percentage = round(float(testScore / maxScore),2)
print("You got", testScore, "out of", maxScore, "on", testName, "which is", percentage * 100, "%")

if percentage >= 0.9:
    print("You got an A in " + testName + " 😍")
elif percentage >= 0.8:
    print("You got a B in " + testName + " 🥰")
elif percentage >= 0.7:
    print("You got a C in " + testName + " 😉")
elif percentage >= 0.6:
    print("You got a D in " + testName + " 😵‍💫")
else:
    print("You got an U in " + testName + " 👻")