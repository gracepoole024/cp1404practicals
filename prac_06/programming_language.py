"""CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimated: 20 minutes
Actual: 17 minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of programming languages"""
        return f"{self.name}, {self.typing}, Reflection = {self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Return representation of strings of programming languages"""
        return str(self)
