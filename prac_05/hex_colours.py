"""
CP1404/CP5632 Practical
Hex Colours
"""
COLOUR_CODES = {"darkslateblue": "#483d8b", "goldenrod": "#daa520", "green4": "#008b00", "mediumspringgreen": "#00fa9a",
                "orchid": "#da70d6", "purple": "#a020f0", "red1": "	#ff0000", "royalblue": "#4169e1",
                "steelblue": "#4682b4", "yellowgreen": "#9acd32"}


def main():
    colour = input("Enter colour name: ").lower
    while colour != "":
        if colour in COLOUR_CODES:
            print(f"{colour} is {COLOUR_CODES[colour]}")
        else:
            print("Invalid colour name.")
        colour = input("Enter colour name: ").lower


if __name__ == '__main__':
    main()