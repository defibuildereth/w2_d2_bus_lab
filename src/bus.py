class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def get_current_capacity(self):
        return self.capacity - len(self.passengers)

    def pick_up_from_stop(self, stop):
        for passenger in stop.queue:
            self.pick_up(passenger)
        stop.queue.clear()