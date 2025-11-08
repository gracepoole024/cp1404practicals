"""CP1404 Practical 7 - Guitars Intermediate Exercise"""
from operator import attrgetter

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))

        name = input("Name: ")
        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost: 5} added")
            name = input("Name: ")

        max_name_length = max(len(guitar.name) for guitar in guitars)
        guitars.sort(reverse=True)
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")

        with open(FILENAME, "w") as out_file:
            for guitar in guitars:
                out_file.write(f"{guitar.name},{guitar.year}, {guitar.cost}")
        print(f"{len(guitars)} saved to {FILENAME}")


main()
