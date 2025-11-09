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
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            projects = add_new_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>").upper()


def read_projects_file(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")  # Split by tab not '
            projects.append(Project(parts[0], (parts[1]), int(parts[2]), float(parts[3]), float(parts[4])))
    return projects


def display_projects(projects):
    for project in projects:
        print(
            f"{project.name}, {project.start_date}, {project.priority}, {project.cost}, {project.completion_percentage}")


def add_new_project(projects):
    """Add a project by prompting user for project details."""
    name = input("Project Name: ")
    start_date = input("Start Date: ")
    priority = int(input("Priority: "))
    cost = float(input("Estimated Cost: "))
    completion_percentage = float(input("Completion Percentage: "))
    projects.append(Project(name, start_date, priority, cost, completion_percentage))
    return projects


if __name__ == '__main__':
    main()
