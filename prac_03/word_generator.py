"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random


def main():
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    print('Enter a string of either "c" or "v" to make a word')
    word_format = input('Enter string: ').lower()
    while not is_valid_format(word_format):
        print('You must only enter "v" or "c" without spaces.')
        word_format = input('Enter string: ').lower()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(string):
    """Determine whether a string is a valid format."""
    for char in string:
        if char != 'c' or char != 'v':
            return False
    return True
