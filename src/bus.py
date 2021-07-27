class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.reduced_rate = price / 2
        self.passengers = []
        self.cash = 0   #no change given, does not have any cash to start with

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        # if person.can_afford
        if person.age >15 and person.age < 66:
            person.reduce_cash(self.price)
            self.cash += self.price
        else:
            person.reduce_cash(self.reduced_rate)
            self.cash += self.reduced_rate
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def get_current_capacity(self):
        return self.capacity - len(self.passengers)

    def pick_up_from_stop(self, stop):
        if self.get_current_capacity() > 0:
            for passenger in stop.queue:
                if passenger.destination == self.destination:
                    self.pick_up(passenger)
                else:
                    print("Wrong bus for you")
        stop.queue.clear()

    def total_cash_on_bus(self):
        return self.cash

    def check_destinations(self):
        for passenger in self.passengers:
            if passenger.destination != self.destination:
                print("Somebody's on the wrong bus")
                return False
        return True
