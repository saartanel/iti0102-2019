"""AOC day 3."""

with open("day3.txt", "r") as big_data:
    def worm():
        """Do big data."""
        coordinates = [0, 0]
        locations = []
        steps = 0
        for move in big_data.readline().split(","):
            direction = move[0]
            move = move.replace(move[0], "")
            times = int(move)
            for _ in range(times):
                if direction == "R":
                    coordinates[0] += 1
                elif direction == "L":
                    coordinates[0] -= 1
                elif direction == "U":
                    coordinates[1] += 1
                elif direction == "D":
                    coordinates[1] -= 1
                steps += 1
                locations.append(tuple(coordinates))
        return locations
    unique = set(worm())
    somelist = []
    for loc in worm():
        if loc in unique:
            somelist.append(abs(loc[0]) + abs(loc[1]))
    print(min(somelist))

with open("day3.txt", "r") as big_data:
    def worm_part2():
        """Do big data."""
        coordinates = [0, 0]
        locations = []
        steps = 0
        for move in big_data.readline().split(","):
            direction = move[0]
            move = move.replace(move[0], "")
            times = int(move)
            for _ in range(times):
                if direction == "R":
                    coordinates[0] += 1
                elif direction == "L":
                    coordinates[0] -= 1
                elif direction == "U":
                    coordinates[1] += 1
                elif direction == "D":
                    coordinates[1] -= 1
                steps += 1
                append = (tuple(coordinates), steps)
                locations.append(append)
        return locations
    somedict = {}
    for loc, steps in worm_part2():
        if loc not in somedict:
            somedict[loc] = steps
    somelist_2 = []
    for loc, steps in worm_part2():
        if loc in somedict:
            somelist_2.append(steps + somedict[loc])
    print(min(somelist_2))
