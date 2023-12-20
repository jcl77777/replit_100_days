def announce(f):
    #Modified wrapper to accept *args (Arbitrary Positional Arguments) and **kwargs (Arbitrary Keyword Arguments). using both accept any combination of positional and keyword arguments.
    def wrapper(*args, **kwargs):
        print("About to check the flight availability...")
        result = f(*args, **kwargs)
        print("Done with checking.")
        return result
    return wrapper

class Flight():
    #define the primary variable: capacity and passenger list. Goal is to ensure the flight would not be overbooked. 
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #for every passenger to book the flight, if capacity is allowed, add to passenger list. if not, return not allowed messages. 
    @announce
    def add_passenger(self, name):
        # if self.open_seats == 0:
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    #to check if the capacity is enough for the amount of passengers
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    # if flight.add_passenger(person):
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")