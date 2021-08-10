"""
CP1404/CP5632 - Practical
A program to read floats from a file as fahrenheit and write them as celsius values to a file
"""
IN_FILE_NAME = "temps_input.txt"
OUT_FILE_NAME = "temps_output.txt"


def main():
    in_file = open(IN_FILE_NAME, 'r')
    out_file = open(OUT_FILE_NAME, 'a')
    for line in in_file:
        converted_value = convert_fahrenheit_to_celsius(float(line.strip()))
        out_file.write(f"{converted_value}\n")
    in_file.close()
    out_file.close()


def convert_celsius_to_fahrenheit(fahrenheit):
    """Convert celsius to fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_fahrenheit_to_celsius(celsius):
    """Convert fahrenheit to celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
