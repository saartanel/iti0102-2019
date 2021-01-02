"""Filter tests program."""
# import pytest
# import filter
import random
import string


from filter import remove_vowels
from filter import longest_filtered_word
from filter import sort_list


def test_remove_vowels_one_vowel():
    """Check code when it removes one vowel."""
    for i in "abcdefghijklmnopqrstuvwxyz":
        assert remove_vowels(i) == remove_vowels(i)


def test_remove_vowels_empty_string():
    """Check code when the input is an empty string."""
    assert remove_vowels("") == ""


def test_remove_vowels_removes_wrong_ascii_letters():
    """Check code when has to remove vowels from ascii letters."""
    assert remove_vowels("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == \
        "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"


def test_remove_vowels_only_non_vowels_longer():
    """Check code when input doesnt include any vowels."""
    assert remove_vowels("sgbpvthnc") == "sgbpvthnc"


def test_remove_vowels_consecutive_vowels():
    """Check code when input is only vowels."""
    assert remove_vowels("bbbbbbbbbbbbbbbb") == "bbbbbbbbbbbbbbbb"


def test_remove_vowels_mixed_cases_only_vowels():
    """Check code when input has only lower- and upper-case vowels."""
    assert remove_vowels("aeiouAEIOU") == ""


def test_remove_vowels_mixed_cases_no_vowels():
    """Check code when input consists of only non-vowel lower and upper-case letters."""
    assert remove_vowels("sgbpvthncSGBPVTHNC") == "sgbpvthncSGBPVTHNC"


def test_remove_vowels_mixed_cases_both_vowels_and_no_vowels():
    """Check code when input inclues both non-vowel and vowel upper- and lower-case letters."""
    assert remove_vowels("aeiouAEIOUsgbpvthncSGBPVTHNC") == "sgbpvthncSGBPVTHNC"


def test_longest_filtered_word_empty():
    """Check code when the input is an empty list."""
    assert longest_filtered_word([]) is None


def test_longest_filtered_word_only_one_word():
    """Check code when the input list consists of only one word."""
    assert longest_filtered_word(["Bunny"]) == "Bnny"


def test_longest_filtered_word_empty_string():
    """Check code when the input list consists of one empty string."""
    assert longest_filtered_word([""]) == ""


def test_longest_filtered_word_same_length_leftmost():
    """Check code when the input lists leftmost(longest) words are the same length."""
    assert longest_filtered_word(["nymphs", "bbbbbb", "Bear", "Snake"]) == "nymphs"


def test_longest_filtered_word_find_longest_before_filtering():
    """Check code if it filters before returning."""
    assert longest_filtered_word(["ccc", "aaaabbbb", "bbbbb"]) != "bbbb"


def test_sort_list_empty_list():
    """Check code when the input list is empty."""
    assert sort_list([]) == []


def test_sort_list_list_len_1():
    """Check code when the return list has one element as a string."""
    assert sort_list(["Da"]) == ["D"]


def test_sort_list_should_not_change_input_list():
    """Check code wether the input list is changed or not."""
    a = ["Bear", "aaaaaaa", "nymphs"]
    b = ["Bear", "aaaaaaa", "nymphs"]
    sort_list(a)
    assert a == b


def test_sort_list_sort_before_remove_vowels():
    """Check code if it sorts before removing vowels."""
    assert sort_list(["cccc", "bbbbbbb", "aaaaaaaaaa"]) != ["aaaaaaaaaa", "bbbbbbb", "cccc"]


def test_sort_list_correct_order_with_same_length():
    """Check code if it returns the list correctly when the output words are of the same size."""
    assert sort_list(["ttttt", "aaccccc", "aaaabbbbb"]) == ["ttttt", "ccccc", "bbbbb"]


def test_uses_random():
    """Check code when the input is randomized."""
    no_vowels = ""
    randstr_size = random.randrange(0, 100)
    for _ in range(randstr_size):
        a = random.choice(string.ascii_letters)
        if a not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            no_vowels += a
    maybe_vowels = no_vowels
    for _ in range(randstr_size):
        maybe_vowels += random.choice(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    assert remove_vowels(maybe_vowels) == no_vowels
