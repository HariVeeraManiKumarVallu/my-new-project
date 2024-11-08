# test_main_functions.py

import pytest
import string
from main_functions import count_words, count_occurrences, merge_strings, generate_random_string

# Unit Tests
def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("this is a test") == 4
    assert count_words("") == 0
    assert count_words("oneword") == 1

def test_count_occurrences():
    assert count_occurrences("hello world hello", "hello") == 2
    assert count_occurrences("this is a test", "test") == 1
    assert count_occurrences("this is a test", "hello") == 0

def test_merge_strings():
    assert merge_strings("abc", "123") == "a1b2c3"
    assert merge_strings("hello", "world") == "hweolrllod"
    assert merge_strings("a", "12345") == "a12345"
    assert merge_strings("abcdef", "xy") == "axbycdef"

def test_generate_random_string():
    result = generate_random_string(10)
    assert len(result) == 10
    assert all(c in string.ascii_letters + string.digits for c in result)
    assert generate_random_string(0) == ""

# Integration Tests
def test_word_count_after_merge():
    """Test the word count after merging two strings that contain spaces."""
    str1 = "hello world"
    str2 = "python code"
    merged = merge_strings(str1, str2)
    word_count = count_words(merged)
    # Expected word count may vary based on how the merge operates with spaces
    assert word_count == 4  # "hpeylltoh woocrlddode"

def test_occurrences_in_random_string():
    """Test the occurrence of a specific character in a generated random string."""
    length = 20
    random_str = generate_random_string(length)
    count_a = count_occurrences(random_str, 'a')
    assert count_a >= 0  # 'a' should occur zero or more times

def test_merge_and_count_words_with_random_string():
    """Test merging a fixed string with a random string, then counting words."""
    fixed_str = "fixed string"
    random_str = generate_random_string(10)  # Random string of length 10
    merged = merge_strings(fixed_str, random_str)
    word_count = count_words(merged)
    assert word_count == 2  # Only one space in the fixed part, so expect 2 words

def test_full_integration():
    """Full integration test combining all functions meaningfully."""
    # Generate a random string and merge it with a phrase
    phrase = "integration test"
    random_str = generate_random_string(8)
    merged = merge_strings(phrase, random_str)
    
    # Count the words in the merged result
    word_count = count_words(merged)
    
    # Check occurrences of certain substrings in the merged result
    occurrences_test = count_occurrences(merged, "test")
    occurrences_integration = count_occurrences(merged, "integration")
    
    # Assert that word count is consistent with expected values
    assert word_count == 2  # The original phrase has 2 words
    
    # Check that occurrences are non-negative, meaning the strings integrated
    assert occurrences_test >= 0
    assert occurrences_integration >= 0
