"""CP1404/CP5632 Practical - Playing the Guitars."""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost: 5} added")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:  # lists, strings and other collections are False when empty, True when non-empty
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    else:
        print("Go buy a guitar")


main()
