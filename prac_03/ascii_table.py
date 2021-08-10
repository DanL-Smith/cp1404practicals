"""
CP1404/CP5632 - Practical
A program to allow user to input a character and see the corresponding ASCII code, and visa versa.
"""
MINIMUM_AMOUNT = 33
MAXIMUM_AMOUNT = 127


def main():
    character = input('Enter a character: ')
    print(f"The ASCII code for {character} is {ord(character)}")
    number = int(input(f'Enter a number between {MINIMUM_AMOUNT} and {MAXIMUM_AMOUNT}: '))
    while not is_valid_number(number):
        print(f"You must enter a number between {MINIMUM_AMOUNT} and {MAXIMUM_AMOUNT}.")
        number = int(input(f'Enter a number between {MINIMUM_AMOUNT} and {MAXIMUM_AMOUNT}: '))
    print(f"The character for {number} is {chr(number)}")
    print()
    display_ascii_values()

def is_valid_number(number):
    if MINIMUM_AMOUNT <= number <= MAXIMUM_AMOUNT:
        return True
    else:
        return False


def display_ascii_values():
    print("ASCII values:")
    for i in range(MINIMUM_AMOUNT, MAXIMUM_AMOUNT):
        print(f"{i:<4d} {chr(i)}")
        print("-------")


main()
