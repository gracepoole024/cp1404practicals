"""CP1404/CP5632 Practical - Guitar class."""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Get age in years of a guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE

    def __str__(self):
        """Return a string representation of a guitar."""
        return f"{self.name} ({self.get_age()}) : ${self.cost}"
