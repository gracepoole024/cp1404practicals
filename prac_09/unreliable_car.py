"""CP1404 Prac 9 - UnreliableCar SubClass"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an instance of a UnreliableCar class, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability percentage."""
        return f"{super().__str__()}, {self.reliability}% reliable"

    def drive(self, distance):
        """Generate random float to determine if car is safe to drive."""
        random_float = random.random(0, 100)
        if self.reliability > random_float:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
