"""CP1404 Practical 7 - Project class"""


class Project:
    """Represent a Project object."""

    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion_percentage=0.0):
        """Initialise a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Compare projects by priority."""
        return self.priority < other.priority

    def __str__(self):
        """Represent project details as a string."""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.completion_percentage}"

    def __repr__(self):
        """Return a string representation of the projects."""
        return str(self)
