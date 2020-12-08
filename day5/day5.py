import math


def get_seat_id(seat_str):
    min_row = 0
    max_row = 127
    for c in seat_str[:7]:
        # going by example in question, floor when taking lower half, ceil when taking lower upper half
        if c == "F":
            max_row = math.floor(max_row - (max_row - min_row) / 2)
        else:
            min_row = math.ceil(min_row + (max_row - min_row) / 2)
        print(f"each iter: {max_row=} {min_row=}")
    print(f"{max_row=} {min_row=}")

    min_col = 0
    max_col = 7
    for c in seat_str[7:]:
        if c == "L":
            max_col = math.floor(max_col - ((max_col - min_col) / 2))
        else:
            min_col = math.ceil(min_col + ((max_col - min_col) / 2))
        print(f"each iter: {max_col=} {min_col=}")
    print(f"{max_col=} {min_col=}")

    print(f"seat ID = {min_row * 8 + min_col}")
    return min_row * 8 + min_col


with open('./input.txt') as file:
    get_seat_id("BFFFBBFRRR")
    ids = [get_seat_id(line.strip()) for line in file]
    print(f"Part 1: max ids = {max(ids)}")

    missing_ids = []
    for i in range(2**10+1):
        if i not in set(ids):
            missing_ids.append(i)
    print(f"Part 2 {missing_ids=}")
    # manually looking at the list, it goes 0, 1, .. 11, 12, 731, 881, 882, ...
    # so 731 is the answer
    