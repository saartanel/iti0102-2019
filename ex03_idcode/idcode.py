# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def get_gender(gender: int) -> str:
    """
    Check if gender is either male or female in ID code.

    :param gender:
    :return: str
    """
    if gender in [1, 3, 5]:
        gender = "male"
    elif gender in [2, 4, 6]:
        gender = "female"

    return gender


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number in range(1, 7):
        return True
    return False


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if 0 <= int(year_number) < 100:
        return True
    return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 0 < month_number <= 12:
        return True
    else:
        return False


def is_leap_year(year: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param year: int
    :return: boolean
    """
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    year = get_full_year(gender_number, year_number)
    leap_year = is_leap_year(int(year))
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        day_in_month = 31
    elif month_number in [4, 6, 9, 11]:
        day_in_month = 30
    else:
        if leap_year:
            day_in_month = 29
        else:
            day_in_month = 28

    if day_number in range(1, (day_in_month + 1)):
        return True
    return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if birth_number in range(1, 1000):
        return True
    return False


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    check_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check_sum = 0
    for i in range(10):
        check_sum += int(id_code[i]) * check_numbers[i]
        check_sum = check_sum % 11
    if check_sum == 10:
        check_numbers = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        check_sum = 0
        for i in range(10):
            check_sum += int(id_code[i]) * check_numbers[i]
            check_sum = check_sum % 11
    if check_sum == int(id_code[-1]):
        return True
    return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    year = ""
    year_digit = len(str(year_number))
    if year_digit == 1:
        if gender_number == 1 or gender_number == 2:
            year = "18"
        elif gender_number == 3 or gender_number == 4:
            year = "19"
        elif gender_number == 5 or gender_number == 6:
            year = "20"
        full_year = int(str(year) + "0" + str(year_number))
    else:
        if gender_number == 1 or gender_number == 2:
            year = "18"
        elif gender_number == 3 or gender_number == 4:
            year = "19"
        elif gender_number == 5 or gender_number == 6:
            year = "20"
        full_year = int(str(year) + str(year_number))
    return full_year


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    birth_place = {
        "Kuressaare": [range(1, 11)],
        "Tartu": [range(11, 21), range(271, 371)],
        "Tallinn": [range(21, 221), range(471, 491)],
        "Kohtla-Järve": [range(221, 271)],
        "Narva": [range(371, 421)],
        "Pärnu": [range(421, 471)],
        "Paide": [range(491, 521)],
        "Rakvere": [range(521, 571)],
        "Valga": [range(571, 601)],
        "Viljandi": [range(601, 651)],
        "Võru": [range(651, 711)],
        "undefined": [range(711, 1000)]
    }
    error = "Wrong input!"
    for city in birth_place:
        range_list = birth_place[city]
        for i in range_list:
            while birth_number in i:
                return city
    else:
        return error


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_id_valid(str(id_code)):
        gender_number = int(id_code[0:1])
        day = id_code[5:7]
        month = id_code[3:5]
        year = id_code[1:3]
        gender = get_gender(gender_number)
        full_year = str(get_full_year(gender_number, int(year)))
        location = get_birth_place(int(id_code[7:10]))
        return "This is a " + gender + " born on " + day + "." + month + "." + full_year + " in " + location + "."
    return "Given invalid ID code!"


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if id_code.isdigit():
        if len(str(id_code)) == 11:
            id_code = str(id_code)
            gender_number = int(id_code[0:1])
            day = int(id_code[5:7])
            month = int(id_code[3:5])
            year = id_code[1:3]
            birth_number = id_code[7:10]
            if is_valid_gender_number(gender_number) \
                    and is_valid_year_number(int(year)) \
                    and is_valid_month_number(int(month)) \
                    and is_valid_day_number(gender_number, int(year), int(month), int(day)) \
                    and is_valid_birth_number(int(birth_number)) \
                    and is_valid_control_number(str(id_code)):
                return True
            return False
        return False
    return False


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(0))  # -> true
    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False
    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
    print("\nControl number:")
    print(is_valid_control_number("50003072738"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nFull message:")
    print(get_data_from_id("50003072738"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    # Comment these back in if you have completed other functions.
    print("\nChecking where the person was born")

    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nOverall ID check::")
    print(is_id_valid("50003072738"))  # -> True
    print(is_id_valid("39909152748"))  # -> False
    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True
