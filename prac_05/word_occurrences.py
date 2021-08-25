"""
CP1404/CP5632 Practical
Word Occurrences
"""
from collections import OrderedDict

text = input("text: ")
word_count = {word: text.count(word) for word in text.split()}
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(f"{word} : {word_count[word]}")
