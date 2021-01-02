"""KT2 (R10)."""


def switch_lasts_and_firsts(s: str):
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    a = s[:2:]
    b = s[2:-2]
    c = s[-2:]
    d = []
    reversed(s)
    if len(s) < 4:
        for i in s:
            d.insert(0, i)
        return "".join(d)
    return c + b + a


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times.

    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if nums.count(7) == 3:
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == nums[i + 1]:
                    return False
            elif i == len(nums) - 1:
                if nums[i] == nums[i - 1]:
                    return False
            else:
                if nums[i] == nums[i + 1] or nums[i] == nums[i - 1]:
                    return False
        return True
    else:
        return False


def g_happy(s):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    if not s:
        return True
    if len(s) < 2:
        return False
    for i in range(len(s)):
        if s[i] == "g":
            if i == 0:
                if s[i + 1] != "g":
                    return False
            elif i == len(s) - 1:
                if s[i - 1] != "g":
                    return False
            else:
                if s[i + 1] != "g" and s[i - 1] != "g":
                    return False
    return True


if __name__ == '__main__':
    print(g_happy(""))  # = > True
