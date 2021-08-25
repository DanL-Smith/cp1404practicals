"""
CP1404/CP5632 Practical
Word Occurrences
"""
from collections import OrderedDict

text = input("text: ")
word_count = {word: text.count(word) for word in text.split()}
for word, count in word_count.items():
    print(f"{word} : {count}")
