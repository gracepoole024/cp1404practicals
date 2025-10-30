"""CP1404/CP5632 Practical - ProgrammingLanguage class."""

"""
Estimated: 20 minutes
Actual: 
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, language="", typing="", reflection="", year=0):
        """Initialise a programming language instance."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.language}, {self.typing}, Reflection = {self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return str(self)
