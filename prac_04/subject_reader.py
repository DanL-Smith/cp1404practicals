"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def print_subject_details(data):
    format_width = max(len(str(x)) for sublist in data for x in sublist) # assigns the largest len element in data to variable
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]:<{format_width}} and has {data[i][2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


main()
