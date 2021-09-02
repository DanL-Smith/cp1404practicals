"""CP1404/CP5632 Practical - Guitars"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = get_guitars()
    print("These are my guitars:")
    print_guitars(guitars)


def print_guitars(guitars):
    """Print information about stored guitars"""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:{max(len(guitar.name) for guitar in guitars)}} ({guitar.year}), worth ${guitar.cost:.2f} {vintage_string}")


def get_guitars():
    """Create guitar instances and return them as a list"""
    guitars = []
    name = input("Name: ")
    while name != '':
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return guitars


if __name__ == "__main__":
    main()
