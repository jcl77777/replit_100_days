genYear = int(input("What is your birth year? "))

if genYear > 1925 and genYear < 1946:
    print("Traditionalists")
elif genYear > 1946 and genYear < 1965:
    print("Baby Boomers")
elif genYear > 1964 and genYear < 1981:
    print("Generation X")
elif genYear > 1980 and genYear < 1997:
    print("Millennials")
elif genYear > 1996 and genYear < 2013:
    print("Generation Z")
else:
    print("Unknown Generation")
