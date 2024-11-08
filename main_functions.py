#main_functions.py

import random
import string

def count_words(text):
    """Counts the number of words in a string."""
    if not text.strip():
        return 0
    return len(text.split())

def count_occurrences(text, word):
    """Counts the occurrences of a word in a string."""
    return text.split().count(word)

def merge_strings(str1, str2):
    """Merges two strings with a space in between."""
    return f"{str1} {str2}"

def generate_random_string(length=5):
    """Generates a random string of a given length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
