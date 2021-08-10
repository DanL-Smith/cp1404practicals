"""
CP1404/CP5632 - Practical
A program to generate 15 random floats between -200 and +200 and write them to a file
"""
import random


def main():
    out_file = open("temps_input.txt", 'a')
    for i in range(15):
        out_file.write(f"{str(random.uniform(-200, 200))}\n")
    out_file.close()


main()
