"""Exam time."""


def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.

    If duplicate keys in the new dictionary exist, leave the first one.
    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}
    :param dic: original dictionary
    :return: dictionary where keys and values are swapped
    """
    d = {}
    for i in dic:
        d[dic[i]] = i
    return d


def find_divisors(number) -> list:
    """
    The task is to find all the divisors for given number in range to the given number's value.

    Divisor - a number that divides evenly into another number.
    Return list of given number divisors in ascending order.
    NB! Numbers 1 and number itself must be excluded if there are more divisors
    than 1 and number itself!
    (138) > [2, 3, 6, 23, 46, 69]
    (3) > [1, 3]
    :param number: int
    :return: list of number divisors
    """
    a = []
    for i in range(number + 1):
        if i and number % i == 0:
            a.append(i)
    if len(a) > 2:
        a.remove(1)
        a.remove(number)
    return a


def sum_of_multiplies(first_num, second_num, limit) -> int:
    """
    The task is to find all the multiplies of each given of two numbers within the limit.

    Then, find the sum of those multiplies.
    (3, 5, 20) => 98 (3 + 6 + 9 + 12 + 15 + 18 + 5 + 10 + 20) 15 is included only once
    (3, 3, 10) => 18 (3 + 6 + 9)
    (3, 10, 2) => 0
    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    a = []
    x = 1
    d = 1
    while True:
        i = x * first_num
        if i <= limit:
            a.append(i)
            x += 1
        else:
            break
    while True:
        i = d * second_num
        if i <= limit:
            a.append(i)
            d += 1
        else:
            break
    return sum(set(a))


def count_odds_and_evens(numbers: list) -> str:
    r"""
    The task is to count how many odd and even numbers does the given list contain.

    Do not count zeros (0).
    Result should be displayed as string "ODDS: {number of odds}\nEVENS: {number of evens}"
    count_odds_and_events([1, 2, 3]) => "ODDS: 2\nEVENS: 1"
    count_odds_and_events([1, 0]) => "ODDS: 1\nEVENS: 0"

    :param numbers: list
    :return: str
    """
    odds = 0
    evens = 0
    for i in numbers:
        if i:
            if i % 2 == 1:
                odds += 1
            elif i % 2 == 0:
                evens += 1
    return f"ODDS: {odds}\nEVENS: {evens}"


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.
    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5
    """
    a = 0
    sum_check = False
    for i in numbers:
        if sum_check and i != 5:
            a += i
        elif i == 2:
            sum_check = True
        elif i == 5:
            sum_check = False
    return a


def transcribe(dna_strand: str):
    """
    Write a function that returns a transcribed RNA strand from the given DNA strand.

    that is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
    Return None if it is not possible to transcribe a DNA strand.
    Empty string should return empty string.
    "ACGTGGTCTTAA" => "UGCACCAGAAUU"
    "gcu" => None
    "a" => "U"

    :param dna_strand: original DNA strand
    :return: transcribed RNA strand in the uppercase or None
    """
    a = {
        "g": "C",
        "c": "G",
        "t": "A",
        "a": "U",
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    b = ""
    for i in dna_strand:
        if i in a:
            b += a[i]
        else:
            return None
    return b


def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    a = {}
    for i in d1:
        if i in d2 and d1[i] == d2[i]:
            a[i] = d1[i]
    return a


def reserve_list(input_strings: list) -> list:
    """
    Given list of strings, return new reversed list where each list element is.

    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed
    ['apple', 'banana', 'onion'] -> ['noino', 'ananab', 'elppa']
    ['lollipop', 'python', 'candy'] -> ['candy', 'python', 'popillol']
    ['sky', 'python', 'candy', 'java', 'fly'] -> ['ylf', 'java', 'candy', 'python', 'yks']
    ['sky', 'python', 'java', 'candy'] -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    reverse_mode = True
    a = []
    for i in input_strings:
        if i == "java":
            reverse_mode = True
            a.insert(0, i)
        elif i == "python":
            reverse_mode = False
            a.insert(0, i)
        else:
            if reverse_mode:
                a.insert(0, i[::-1])
            else:
                a.insert(0, i)
    return a


def convert_binary_to_decimal(binary_list: list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.

    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    a = 0
    b = len(binary_list) - 1
    for i in binary_list:
        a += i * (2 ** b)
        b -= 1
    return a


def print_pages(pages: str) -> list:
    """
    Find pages to print in console.

    examples:
    print_pages("2,4,9") -> [2, 4, 9]
    print_pages("2,4-7") -> [2, 4, 5, 6, 7]
    print_pages("2-5,7,10-12,17") -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
    print_pages("1,1") -> [1]
    print_pages("") -> []
    print_pages("2,1") -> [1, 2]

    :param pages: string containing page numbers and page ranges to print.
    :return: list of pages to print with no duplicates, sorted in increasing order.
    """
    a = pages.split(",")
    b = []
    if not pages:
        return []
    for i in a:
        if "-" in i:
            c = i.split("-")
            for j in range(int(c[0]), int(c[1]) + 1):
                b.append(j)
        else:
            b.append(int(i))
    return sorted(list(set(b)))


if __name__ == '__main__':
    print(find_divisors(138))  # > [2, 3, 6, 23, 46, 69]
    print(find_divisors(3))  # > [1, 3])
