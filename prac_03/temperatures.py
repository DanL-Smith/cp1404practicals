"""
CP1404/CP5632 - Practical
A program to convert celsius to fahrenheit and visa versa
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_celsius_to_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} F")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(fahrenheit):
    """Convert celsius to fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_fahrenheit_to_celsius(celsius):
    """Convert fahrenheit to celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
