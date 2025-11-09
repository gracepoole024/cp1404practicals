"""
CP1404 Practical 7 - Project Management Program
Estimated time:3hrs
Actual time:
"""
from datetime import datetime
from operator import attrgetter

from prac_07.project import Project

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
    filename = input("Enter filename: ")
    projects = read_projects_file(filename)
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
            filter_projects_by_date(projects)
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
    projects.sort(reverse=True)
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


def filter_projects_by_date(projects):
    input_date = input("Show projects after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(input_date, "%d/%m/%Y")

    filtered_dates = []
    for project in projects:
        project_date = datetime.strptime(project.start_date, "%d/%m/%Y")
        if project_date >= filter_date:
            filtered_dates.append(project)

    filtered_dates.sort(key=attrgetter('start_date'))

    for project in filtered_dates:
        print(project)


if __name__ == '__main__':
    main()
