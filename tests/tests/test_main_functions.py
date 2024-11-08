from main_functions import count_words, count_occurrences, merge_strings, generate_random_string

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("this is a test") == 4
    assert count_words("") == 0

def test_count_occurrences():
    assert count_occurrences("hello world hello", "hello") == 2
    assert count_occurrences("this is a test", "test") == 1
    assert count_occurrences("this is a test", "hello") == 0

def test_merge_strings():
    assert merge_strings("hello", "world") == "hello world"
    assert merge_strings("foo", "bar") == "foo bar"

def test_generate_random_string():
    random_string = generate_random_string(10)
    assert isinstance(random_string, str)
    assert len(random_string) == 10

# Integration Test
def test_integration():
    text = "hello world hello"
    word_count = count_words(text)
    word_occurrences = count_occurrences(text, "hello")
    assert word_count == 3
    assert word_occurrences == 2
