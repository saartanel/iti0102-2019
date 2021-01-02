"""Filtering."""


def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in vowel:
        string = string.replace(letter, "")
    return string


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    Return None if list is empty.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    newlist = []
    if not string_list:
        return None
    else:
        for word in string_list:
            word = remove_vowels(word)
            newlist.append(word)
        return max(newlist, key=len)


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    Longer strings come first.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order.
    """
    newlist = []
    if not string_list:
        return newlist
    else:
        for word in string_list:
            word = remove_vowels(word)
            newlist.append(word)
        newlist.sort(key=len, reverse=True)
        return newlist


if __name__ == '__main__':
    print(remove_vowels(""))  # => ""
    print(remove_vowels("hello"))  # => "hll"
    print(remove_vowels("Home"))  # => "Hm"
    print(longest_filtered_word(["Bunny", "Tiger", "Bear", "Sn"]))  # => "Bnny"
    print(longest_filtered_word([]))
    print(sort_list(["Bunny", "Tiger", "Bear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']
    print(sort_list(["Jeesus", "Kristus", "Captain", "Morgan"]))
    print(sort_list([]))
