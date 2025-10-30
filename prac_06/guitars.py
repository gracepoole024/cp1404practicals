"""CP1404/CP5632 Practical - Playing the Guitars."""
from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost: 5}")
    name = input("Name: ")
print("These are my guitars: ")
print(f"Guitar 1: {name} ({year}), worth ${cost}")

