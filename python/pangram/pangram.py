#!/usr/local/bin/python
import string
def is_pangram(phrase):
    return set(filter(str.isalpha, phrase.lower())) == set(string.lowercase)
