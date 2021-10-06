"""
CP1404/CP5632 Practical
Taxi class
"""
from prac_08.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    PRICE_PER_KM = 1.23

    def __init__(self, name: str = '', fuel: int = 0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.PRICE_PER_KM:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(self.PRICE_PER_KM * self.current_fare_distance, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven