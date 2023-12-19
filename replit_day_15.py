animal = ""
exit_condition = ""
while exit_condition.lower() != "yes":
    animal = input("What animal do you want?: ")
    if animal.lower() == "cow":
        print("A cow goes moo.")
    elif animal.lower() == "lesser spotted lemur":
        print("Ummm... the Lesser Spotted Lemur goes awooga.")
    else: 
      print("I don't know that animal sound. Try again.")
    exit_condition = input("Do you want to exit? (yes/no): ")