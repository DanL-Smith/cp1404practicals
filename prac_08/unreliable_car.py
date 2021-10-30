"""
CP1404/CP5632 Practical
Unreliable Car Class
"""
import random

from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that is unreliable"""

    def __init__(self, name: str = '', fuel=0, reliability: float = 0):
        """Initialise a Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = random.randint(0, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
