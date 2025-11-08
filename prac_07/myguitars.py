"""CP1404 Practical 7 - Guitars Intermediate Exercise"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # skip heading
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], parts[1], parts[2]))
    print(guitars)

main()
