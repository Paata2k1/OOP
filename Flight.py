import random
import string
import names

passengers = []
for i in range(5):
    passengers = names.get_first_name()


class Flight:

    def __init__(self, source, destination, duration, seats, ):
        self.id = id
        self.source = source
        self.destination = destination
        self.duration = duration
        self.seats = seats
        self.passengers = passengers

    def generate_id(self):
        id = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        return id

    def open_seats(self):
        print(self.seats > len(passengers))

    def add_passenger(self):
        if len(passengers) >= self.seats:
            print("No seats available")
        else:
            passengers.append('Liv')
            print(passengers)

    def list_passengers(self):
        for i in range(4):
            passengers = names.get_first_name()
            print(passengers)

    def display_info(self):
        print("Flight ID:" + self.generate_id(), "\nsource:" + self.source, "\nDestination:" + self.destination,
              "\nDuration:" + str(self.duration), "\nSeats:" + str(self.seats))



















