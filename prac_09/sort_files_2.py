"""
CP1404/CP5632 Practical
Sort Files 2
Create directories based on extension categories and move files in to them
"""
import shutil
import os
CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Sort files in to categories"""
    os.chdir(CURRENT_DIRECTORY)
    extensions = set()
    extensions_to_categories = {}

    for file in os.listdir('.'):
        if os.path.isfile(file):
            extension = file.split('.')[1]
            if extension not in extensions:
                extensions.add(extension)
                category = input(f"What category would you like to sort {extension} files into? ")
                extensions_to_categories[extension] = category
                try:
                    os.mkdir(category)
                except FileExistsError:
                    pass
            shutil.move(file, extensions_to_categories.get(extension))


if __name__ == "__main__":
    main()
