"""
CP1404 Practical 7 - Project Management Program
Estimated time:3hrs
Actual time:
"""
from prac_07.project import Project

FILENAME = "projects.txt"

MENU = """Menu:
L - Load Projects
S - Save Projects
D - Display Projects
F - Filter projects by date
A - Add new project
Q - Quit
"""


def main():
    """Interactive program to load and save projects to a text file."""
    projects = read_projects_file(FILENAME)
    print(MENU)
    choice = input(">>").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>").upper()


def read_projects_file(filename):
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            in_file.readline()
            parts = line.strip().split(",")
            projects.append(Project(parts[0], (parts[1]), int(parts[2]), float(parts[3]), float(parts[4])))
