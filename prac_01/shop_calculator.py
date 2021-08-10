"""
Program to calculate the total price for a user specified number of items,
each with a different price.
"""


def main():
    total = 0
    DISCOUNT = 0.10
    print("This program allows you to calculate the total price for a number of items.")
    number_of_items = get_valid_number("Number of items: ")
    for i in range(int(number_of_items)):
        price = get_valid_number(f"Price of item #{i + 1}: ")
        total += price
    if total > 100:
        total -= (total * DISCOUNT)
    print(f"Total price for {int(number_of_items)} items is ${total:.2f}")


def get_valid_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            number = float(input(prompt))
            while number < 0:
                print("You must specify a number greater than or equal to 0.")
                number = float(input(prompt))
            break
        except ValueError:
            print("You must enter a number")
    return number


main()