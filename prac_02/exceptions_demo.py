"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a value that is not an integer is entered
2. When will a ZeroDivisionError occur? When the user tries to divide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes
"""

try:
    while True:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if numerator == 0 or denominator == 0:
            print("Cannot divide by zero!")
            continue
        else:
            fraction = numerator / denominator
            print(fraction)
            break
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")