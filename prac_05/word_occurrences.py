"""
CP1404/CP5632 Practical 5
Word Occurrences Program
"""

"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

from operator import itemgetter

Text = input("Text: ")
words = Text.lower().split()

word_to_occurrence = {word: words.count(word) for word in words}
maximum_word_length = max(len(word) for word in list(word_to_occurrence.keys()))

for word, occurrence in sorted(word_to_occurrence.items(), key=itemgetter(1), reverse=True):
    print(f"{word:{maximum_word_length}}: {occurrence}")
