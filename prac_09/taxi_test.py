"""CP1404 Prac 9 - Test Taxi SubClass."""
from prac_09.taxi import Taxi


def main():
    """Program to text Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi.get_fare())


main()
