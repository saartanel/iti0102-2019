"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    """
    Check if number (given in function parameter) is prime.

    If number is prime -> return True
    If number is not prime -> return False

    :param number: number for check.
    :return: boolean True if number is prime or False if number is not prime.
    """
    if number == 2:
        return True
    if number > 2:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    return False


if __name__ == '__main__':
    print(is_prime_number(0))   # -> False
    print(is_prime_number(1))   # -> False
    print(is_prime_number(2))   # -> True
    print(is_prime_number(3))   # -> True
    print(is_prime_number(4))   # -> False
