"""CP1404 Practical 7 - Guitars Intermediate Exercise"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to add and display guitars in order of age."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))

        receive_new_guitar(guitars)

        max_name_length = max(len(guitar.name) for guitar in guitars)
        display_guitars(guitars, max_name_length)

        write_guitars_to_file(guitars)


def write_guitars_to_file(guitars):
    """Add new guitars received by user to guitars.csv."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year}, {guitar.cost}")
    print(f"{len(guitars)} saved to {FILENAME}")


def display_guitars(guitars, max_name_length):
    """Display guitars from oldest to newest."""
    guitars.sort(reverse=True)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


def receive_new_guitar(guitars):
    """Receive new guitar from user input until string is empty."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost: 5} added")
        name = input("Name: ")


if __name__ == '__main__':
    main()
