"""CP1404 Prac 9 - UnreliableCar test program."""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Program to test UnreliableCar SunClass."""
    good_car = UnreliableCar("Hyundai Getz", 50, 87.9)
    bad_car = UnreliableCar("Prius 1", 100, 7.8)

    for i in range(1, 20):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    print(good_car)
    print(bad_car)


main()
