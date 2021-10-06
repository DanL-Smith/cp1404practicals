"""
CP1404/CP5632 Practical
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test the Unrealiable Car class."""
    my_unreliable_car = UnreliableCar("Beat-up Holden", 100, 77)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)
    print(my_unreliable_car.reliability)
    my_unreliable_car.drive(100)
    print(my_unreliable_car)


if __name__ == "__main__":
    main()
