"""CP1404 Prac 9 - Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Interactive program to use Taxi and SilverServiceTaxi classes."""
    total_fare = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except ValueError:
                print("Invalid taxi choice")
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                cost = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${cost}")
                total_fare += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid menu choice")
        print(f"Bill to date: ${total_fare}")
        print(MENU)
        choice = input(">>").lower()


def drive_taxi(current_taxi):
    current_taxi.start_fare()
    distance = float(input("Drive how far?"))
    current_taxi.drive(distance)
    cost = current_taxi.get_fare()
    return cost


def display_taxis(taxis):
    """Display taxis using an index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
