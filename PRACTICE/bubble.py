class Train:
    def __init__(self, train_name, start, *destinations):
        self.train_name = train_name
        self.start = start
        self.destinations = destinations
        self.passengers = []

    def addPassenger(self, *passengers):
        for passenger in passengers:
            self.passengers.append(passenger)

    def allPassengerDetails(self):
        print(f"Welcome aboard on {self.train_name}")
        print(f"Start: {self.start}")
        print(f"Destination: {self.destinations[-1]}")
        for passenger in self.passengers:
            print(passenger.getDetails(self.destinations))


class Passenger:
    def __init__(self, name, start=None, destination=None):
        self.name = name
        self.start = start
        self.destination = destination

    def getDetails(self, destinations):
        start_index = destinations.index(self.start) if self.start else 0
        destination_index = destinations.index(self.destination) if self.destination else len(destinations) - 1
        total_fare = abs(destination_index - start_index) * 100
        return f"Name: {self.name}, Start: {self.start}, Destination: {self.destination}, Fare: ${total_fare}"


# Driver Code
t1 = Train('T1-Express', 'New York', 'Manhattan', 'Brooklyn', 'Boston')
print("1========================")
p1 = Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke", "Manhattan")
p3 = Passenger("Hinata", "Manhattan", "Brooklyn")
print("2========================")
t1.addPassenger(p2, p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")

t2 = Train('Europe-Express', 'London', 'Paris', 'Brussels', 'Turkey')
print("5========================")
p4 = Passenger("Max", "London", "Brussels")
p5 = Passenger("Eleven", "Paris")
p6 = Passenger("Mike", "Brussels")
t2.addPassenger(p4, p5, p6)
print("6========================")
t2.allPassengerDetails()
