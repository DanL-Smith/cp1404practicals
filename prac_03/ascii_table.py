"""
CP1404/CP5632 - Practical
A program to allow user to input a character and see the corresponding ASCII code, and visa versa.
"""
MINIMUM_AMOUNT = 33
MAXIMUM_AMOUNT = 127


def main():
    character = input('Enter a character: ')
    print(f"The ASCII code for {character} is {ord(character)}")
    number = get_valid_number(f'Enter a number between {MINIMUM_AMOUNT} and {MAXIMUM_AMOUNT}: '
                        , MINIMUM_AMOUNT, MAXIMUM_AMOUNT)
    print(f"The character for {number} is {chr(number)}")
    print()
    display_ascii_values()


def get_valid_number(string, lower, upper):
    """Get a number within a specified range"""
    while True:
        try:
            number = int(input(string))
            while number < lower or number > upper:
                print(f"You must enter a number between {lower} and {upper}.")
                number = int(input(f'Enter a number between {lower} and {upper}: '))
            return number
        except ValueError:
            print('Please enter a valid number!')
            continue


def display_ascii_values():
    """Display ASCII value table"""
    print("ASCII values:")
    for i in range(MINIMUM_AMOUNT, MAXIMUM_AMOUNT):
        print(f"{i:<4d} {chr(i)}")
        print("-------")


main()
