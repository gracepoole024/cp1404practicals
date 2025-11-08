"""CP1404 Practical 7 - Guitars Intermediate Exercise"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))

        guitars.sort(reverse=True)
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


main()
