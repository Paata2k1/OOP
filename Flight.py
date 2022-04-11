import random
import string


class Flight:

    def __init__(self, id, source, destination, duration, seats, passengers):
        self.id = id
        self.source = source
        self.destination = destination
        self.duration = duration
        self.seats = seats
        self.passengers = passengers

    def generate_id(self):
        id = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        return id
