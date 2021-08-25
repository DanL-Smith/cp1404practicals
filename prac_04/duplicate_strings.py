"""
CP1404/CP5632 Practical
Duplicate Strings
"""


def main():
    strings = []

    string = input('Enter string: ')
    while string != '':
        strings.append(string)
        string = input('Enter string: ')

    modified_strings = set()
    duplicates = set()
    for string in strings:
        if string not in modified_strings:
            modified_strings.add(string)
        else:
            duplicates.add(string)
    if len(duplicates) > 0:
        print("Strings repeated:", ", ".join(duplicates))
    else:
        print("No repeated strings entered.")


main()
