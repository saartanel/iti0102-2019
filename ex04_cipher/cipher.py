"""Encode and decode text using Rail-fence Cipher."""


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    message = message.replace(" ", "_")
    table = []
    for _ in range(key):
        row = []
        table.append(row)
        for _ in range(len(message)):
            row.append(".")
    down_move = True
    row = 0
    if key == 1:
        return message
    else:
        for i in range(len(message)):
            if row == 0:
                table[row][i] = message[i]
                row += 1
                down_move = True
            elif row == key - 1:
                table[row][i] = message[i]
                row -= 1
                down_move = False
            elif down_move:
                table[row][i] = message[i]
                row += 1
            elif not down_move:
                table[row][i] = message[i]
                row -= 1
    result = ""
    for row in table:
        result += ("".join(row))
    result = result.replace(".", "")
    return result


def create_table(message: str, key: int) -> list:
    """
    Create table with *-s instead of letters.

    :param message:
    :param key:
    """
    message = message.replace(" ", "_")
    table = []
    for _ in range(key):
        row = []
        table.append(row)
        for _ in range(len(message)):
            row.append(".")
    down_move = True
    row = 0
    if key == 1:
        return message
    else:
        for i in range(len(message)):
            if row == 0:
                table[row][i] = "*"
                row += 1
                down_move = True
            elif row == key - 1:
                table[row][i] = "*"
                row -= 1
                down_move = False
            elif down_move:
                table[row][i] = "*"
                row += 1
            elif not down_move:
                table[row][i] = "*"
                row -= 1
    return table


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    number = 0
    table = create_table(message, key)
    for i, row in enumerate(table):
        for j, char in enumerate(row):
            if char == "*":
                table[i][j] = message[number]
                number += 1
    result = ""
    down_move = True
    row = 0
    if key == 1:
        message = message.replace("_", " ")
        return message
    else:
        for i in range(len(message)):
            if row == 0:
                result += table[row][i]
                row += 1
                down_move = True
            elif row == key - 1:
                result += table[row][i]
                row -= 1
                down_move = False
            elif down_move:
                result += table[row][i]
                row += 1
            elif not down_move:
                result += table[row][i]
                row -= 1
    result = result.replace("_", " ")
    return result


if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello
    print(encode("kaks pead", 1))  # => kaks_pead

    print(decode("kaks_pead", 1))  # => kaks pead
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida
