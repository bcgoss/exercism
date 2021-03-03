def is_isogram(word):
    letters = filter(str.isalpha, word.lower())
    return sorted(set(letters)) == sorted(letters)
