"""CP1404 Practical 7 - Project class"""


class Project:
    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion_percentage=0.0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Represent car details as a string."""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.completion_percentage}"
