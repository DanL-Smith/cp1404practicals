"""
CP1404/CP5632 Practical
Taxi Test
This program tests the Taxi class.
"""

from prac_08.taxi import Taxi


def main():
    """Test the Taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(F"Current fare: ${my_taxi.get_fare()}")


if __name__ == "__main__":
    main()
