"""
CP1404/CP5632 Practical
Sort Files Version 1
Create directories for each unique extension type and sort files in to their respective folders
"""
import shutil
import os
CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Sort files in to extension types."""
    os.chdir(CURRENT_DIRECTORY)
    extensions = set()

    for file in os.listdir('.'):
        if os.path.isfile(file):
            extension = file.split('.')[1]
            if extension not in extensions:
                extensions.add(extension)
                try:
                    os.mkdir(extension)
                except FileExistsError:
                    pass
            shutil.move(file, extension)


if __name__ == "__main__":
    main()
