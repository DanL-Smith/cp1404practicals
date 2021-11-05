"""
CP1404/CP5632 Practical
Taxi Simulator Program
Simulates a Taxi service wherein a user can choose from a list of taxis and determine the bill based on
model and distance travelled
"""
__author__ = "Daniel Smith"

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU_CHOICES = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Lets drive!")
    print(MENU_CHOICES)
    choice = input(">>> ")
    while choice != "q":
        if choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance_travelled = get_valid_distance("Drive how far? ")
                if distance_travelled == 0:
                    print("You stayed still.")
                else:
                    current_taxi.drive(distance_travelled)
                    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
                    total_bill += current_taxi.get_fare()
        elif choice == "c":
            print("Taxis available:")
            current_taxi = get_current_taxi(current_taxi, taxis)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill}")
        print(MENU_CHOICES)
        choice = input(">>> ")

    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(i, " - ", taxi)


def get_valid_distance(prompt: str):
    """Get a number from user that is 0 or greater."""
    while True:
        try:
            number = int(input(prompt))
            while number < 0:
                print('Number must be 0 or greater')
                number = int(input(prompt))
        except ValueError:
            print("You must enter a number")
            continue
        return number


def get_current_taxi(current_taxi, taxis: list):
    """Determine what the current taxi is based on user input."""
    for i, taxi in enumerate(taxis):
        print(i, " - ", taxi)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0:
            print("Number must be > 0.")
            return None
        try:
            current_taxi = taxis[taxi_choice]
            print(f"You chose the {current_taxi.name}")
        except IndexError:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return current_taxi


if __name__ == "__main__":
    main()
