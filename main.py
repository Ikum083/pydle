# Pydle: Python Wordle Clone

# list to contain all words to be used
with open("words.txt") as f:
    words = [line.strip() for line in f]

print(words)