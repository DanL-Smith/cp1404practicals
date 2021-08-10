"""
CP1404/CP5632 - Practical
Program to write to file the status of a user-specified number of random scores
"""
import random


def main():
    out_file = open("results.txt", 'a')
    enumerator = int(input('Enter number of scores: '))
    for i in range(enumerator):
        score = random.randrange(0, 100)
        result = get_score_result(score)
        out_file.write(f"{score} is {result}\n")
    out_file.close()


def get_score_result(score):
    """Determine the result of a score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "bad"
    return result


main()
