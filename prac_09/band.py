"""CP1404 Prac 9 - Band class with association relationship"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Initialise an instance of a Band class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Represent Band class attributes as a string."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to a list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician is playing."""
        for musician in self.musicians:
            print(musician.play())
