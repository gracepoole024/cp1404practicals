"""CP1404 - Practical 2
Program to display menu to get subject score"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Program to display menu and determine score satus"""
    score = int(input("Enter Score: "))
    print(MENU)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_result()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">").upper()
    print("Goodbye")


def get_valid_result():
    """Get valid result from user"""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Enter Score: "))
    return score


def print_result(score):
    """Print status of given score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    """Print number of stars based on score"""
    print("*" * score)


main()
