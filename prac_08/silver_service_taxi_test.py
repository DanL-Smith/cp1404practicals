"""
CP1404/CP5632 Practical
Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the Silver Service class."""
    my_silver_service_taxi = SilverServiceTaxi("First Class Taxi", 100, 2)
    my_silver_service_taxi.start_fare()
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    print(F"Current fare: ${my_silver_service_taxi.get_fare()}")


if __name__ == "__main__":
    main()
