"""CP1404/CP5632 Practical - ProgrammingLanguage class."""

"""
Estimated: 20 minutes
Actual: 
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, typing="", reflection=False, year=0):
        """Initialise a programming language instance."""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic"""
        return self.typing == "Dynamic"


