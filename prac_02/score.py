"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Program to determine score satus"""
    score = float(input("Enter score: "))
    determine_grade(score)


def determine_grade(score: float):
    """Determine status of given score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
