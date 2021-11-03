"""
CP1404/CP5632 Practical
Word Occurrences
"""

text = input("text: ").split()
word_count = {word: text.count(word) for word in text}
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(f"{word:{max(len(word) for word in word_count)}s} : {word_count[word]}")
