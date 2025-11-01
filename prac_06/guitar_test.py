"""CP1404/CP5632 Practical - Test Guitar class program."""

from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Another Guitar", 2016, 1512.9)

print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected 9. Got {other_guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")
