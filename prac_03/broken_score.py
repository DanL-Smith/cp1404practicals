"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(f'Result: {result}')
    random_result = get_score_result(random.randrange(1, 100))
    print(f"Random Result: {random_result}")


def get_score_result(score):
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