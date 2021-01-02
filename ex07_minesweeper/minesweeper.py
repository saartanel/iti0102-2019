"""Minesweeper has to swipe the mines."""
import copy


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    return [["." for _ in range(width)] for _ in range(height)]


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    This function cannot modify the original minefield list.
    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.
    :param minefield: list
    :param mines: list
    :return: list
    """
    mf2 = copy.deepcopy(minefield)
    for bombs in mines:
        for rowi in range(bombs[0], len(mf2) - bombs[1]):
            for coli in range(bombs[3], len(mf2[rowi]) - bombs[2]):
                if mf2[rowi][coli] == "x" or mf2[rowi][coli] == "X":
                    mf2[rowi][coli] = "X"
                else:
                    mf2[rowi][coli] = "x"
    return mf2


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    .....
    .....
    x....
    Xx...

    :param minefield:
    :return:
    """
    return "".join(["".join(i) + "\n" for i in minefield])


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    This function cannot modify the original list.
    So, the result should be a new list (or copy of original).

    ....
    ..x.
    X.X.
    x..X

    =>

    0111
    13x2
    X4X3
    x32X

    :param minefield:
    :return:
    """
    mf2 = copy.deepcopy(minefield)
    for row in range(len(minefield)):
        for col in range(len(minefield[row])):
            count = 0
            for rowi in range(row - 1, row + 2):
                for coli in range(col - 1, col + 2):
                    if 0 <= rowi < len(mf2) and 0 <= coli < len(mf2[row]) and minefield[rowi][coli] in ("x", "X"):
                        count += 1
            if mf2[row][col] == ".":
                mf2[row][col] = str(count)
    return mf2


def walk(minefield, moves, lives) -> list:
    """
    Make moves on the minefield.

    This function cannot modify the original minefield list.
    Starting position is marked by #.
    There is always exactly one # on the field.
    The position you start is an empty cell (".").

    Moves is a list of move "orders":
    N - up,
    S - down,
    E - right,
    W - left.

    Example: "NWWES"

    If the position you have to move contains "x" (small mine),
    then the mine is cleared (position becomes "."),
    but you cannot move there.
    In case of clearing a small mine, ff the position where the minesweeper is, has 5 or more mines nearby
    (see the previous function), minesweeper also loses a life.
    If it has 0 lives left, then clearing is not done and moving stops.

    Example:
    #x
    ..
    moves: ESS

    =>

    1st step ("E"):
    #.
    ..

    2nd step ("S"):
    ..
    #.

    3rd step ("S"):
    ..
    #.

    Example #2
    XXX
    x.x
    .#X
    moves: NWES, lives = 1

    1) "N"
    XXX
    x#x
    ..X

    2) "W". the small mine is cleared, but with the cost of one life :'(
    XXX
    .#x
    ..X
    lives = 0

    3) "E"
    XXX
    .#x
    ..X
    As clearing the mine on the right, he would lose a life (because minesweeper has 5 or more mines nearby).
    But as he has no lives left, he stops there. No more moves will be carried out.

    If the position you have to move contains "X" (huge mine),
    then you move there and lose a life.

    #X
    ..
    moves: ESS

    1) (lives = lives - 1)
    .#
    ..
    2)
    ..
    .#
    3)
    ..
    .#

    If you have to move into a position with a huge mine "X"
    but you don't have any more lives, then you finish your moves.

    lives: 2

    #XXXX
    .....
    moves: EEES

    1) lives = 1
    .#XXX
    .....
    2) lives = 0
    ..#XX
    .....
    3) stop, because you would die
    final result:
    ..#XX
    .....

    :param minefield:
    :param moves:
    :param lives:
    :return:
    """
    mf = copy.deepcopy(minefield)
    cur_row = get_pos(minefield)[0]
    cur_col = get_pos(minefield)[1]
    mf[cur_row][cur_col] = "."
    for move in moves:
        new_row = get_new_number(move, cur_row, cur_col, mf)[0]
        new_col = get_new_number(move, cur_row, cur_col, mf)[1]
        if mf[new_row][new_col] == "x":
            if int(calculate_mine_count(mf)[cur_row][cur_col]) >= 5:
                if lives == 0:
                    break
                else:
                    mf[new_row][new_col] = "."
                    lives -= 1
            else:
                mf[new_row][new_col] = "."
        elif mf[new_row][new_col] == "X":
            if lives == 0:
                break
            else:
                mf[new_row][new_col] = "."
                lives -= 1
                cur_row = new_row
                cur_col = new_col
        elif mf[new_row][new_col] == ".":
            cur_row = new_row
            cur_col = new_col
    mf[cur_row][cur_col] = "#"
    return mf


def get_pos(field):
    """
    Find the "#" in minefield.

    :param field:
    """
    return [(i, field[i].index("#")) for i in range(len(field)) if "#" in field[i]][0]


def get_new_number(move, cur_row, cur_col, field):
    """
    Find new row and new col according to move type.

    :param field:
    :param cur_col:
    :param cur_row:
    :param move:
    """
    new_row = cur_row
    new_col = cur_col
    if move == "N" and 0 < cur_row < len(field) and 0 <= cur_col < len(field[cur_row]):
        new_row = cur_row - 1
        new_col = cur_col
    elif move == "S" and 0 <= cur_row < len(field) - 1 and 0 <= cur_col < len(field[cur_row]):
        new_row = cur_row + 1
        new_col = cur_col
    elif move == "E" and 0 <= cur_row < len(field) and 0 <= cur_col < len(field[cur_row]) - 1:
        new_row = cur_row
        new_col = cur_col + 1
    elif move == "W" and 0 <= cur_row < len(field) and 0 < cur_col < len(field[cur_row]):
        new_row = cur_row
        new_col = cur_col - 1
    return new_row, new_col


if __name__ == '__main__':
    mf = create_minefield(3, 5)
    mf = add_mines(mf, [[0, 0, 1, 2]])
    mf = add_mines(mf, [[0, 1, 1, 1]])
    mf[0][4] = "#"
    mf = walk(mf, "WSSWN", 2)
    print(get_minefield_string(mf))
