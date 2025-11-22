"""CP1404 Prac 9 - Test Program for SilverServiceTaxi test"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Program to test SilverServiceTaxi SubClass."""
    fancy_taxi = SilverServiceTaxi("BMW", 200, 4)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(fancy_taxi.get_fare())


main()
