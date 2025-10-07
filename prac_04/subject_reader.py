"""
CP1404/CP5632 Practical 4
Converting Data Strings to Lists
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data(FILENAME)
    display_subject(subject_data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)
    input_file.close()
    return subject_data


def display_subject(subject_data):
    """Display subject details."""
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:10} and has {subject[2]:4} students")


main()
