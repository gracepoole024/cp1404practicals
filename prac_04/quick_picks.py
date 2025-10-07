"""
CP1404/CP5632 Practical 4
"Quick Pick" Lottery Ticket Generator
"""

from random import randint

NUMBERS_ON_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("Enter positive integer")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []

    for j in range(NUMBERS_ON_LINE):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
