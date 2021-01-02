"""Regex."""
import re


def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    file_list = []
    with open(path, "r") as file:
        for i in file:
            i = i.strip("\n")
            file_list.append(i)
    file_list = list(filter(None, file_list))
    return file_list


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.

    Return all keyword occurrences (case insensitive).
    If an element cointains the keyword several times, count all the occurrences.

    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    number = 0
    keyword = keyword.lower()
    if keyword:
        for i in input_data:
            i = i.lower()
            number += len(re.findall(keyword, i))
        return number
    return number


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.

    Return all unique valid email addresses in alphabetical order presented in the list.
    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    regex = r"([a-zA-Z0-9][a-zA-Z0-9._+-]+\@[a-zA-Z0-9_+-]+(\.[a-zA-Z0-9_+-]+){1,2})"
    email_list = []
    for row in input_data:
        match = re.findall(regex, row)
        for i in match:
            match = i[0]
            if match not in email_list:
                email_list.append(match)
    return sorted(email_list)


if __name__ == '__main__':
    list_of_lines_emails = read_file("input_detect_email_addresses_example_2.txt")  # reading from file
    print(detect_email_addresses(list_of_lines_emails))  # ['allowed@example.com', 'firstname-lastname@example.com',
    # 'right@example.com', 'spoon@lol.co.jp', 'testtest@dome.museum', 'testtest@example.name']

    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")
    print(match_specific_string(list_of_lines_keywords, "job"))  # 9
