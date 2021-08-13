"""
CP1404/CP5632 Practical - Quick Pick Lottery Ticket Generator
A program to generate and print a user-specified number of lines that consist of 6 random numbers
between a minimum and maximum range
"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    number_of_lines = int(input("How many quick picks? "))
    for i in range(number_of_lines):
        numbers = random.sample(range(MINIMUM_NUMBER, MAXIMUM_NUMBER), 6)
        numbers.sort()
        print(*numbers)


main()