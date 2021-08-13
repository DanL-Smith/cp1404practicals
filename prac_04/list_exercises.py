"""
CP1404/CP5632 Practical
Basic List Operations 1
"""


def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    count = 1
    print("Enter a number less than 0 to finish.")
    number = int(input(f"Number {count}: "))
    while number >= 0:
        numbers.append(number)
        count += 1
        number = int(input(f"Number {count}: "))
    print_numbers_facts(numbers)

    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def print_numbers_facts(numbers):
    """Display facts about a list of numbers"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()
