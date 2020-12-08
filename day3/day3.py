# Part 1
tree_count = 0
with open('./input.txt') as file:
    # list of lines, each line represent one row
    input_grid = [line.strip() for line in file]
    original_grid_height = len(input_grid)
    original_grid_width = len(input_grid[0])

    x = y = 0

    def next_position_char() -> str:
        global x, y
        x += 3
        y += 1
        return input_grid[y][x % original_grid_width]

    while y < original_grid_height - 1:
        # print(f"{next_position_char()=}")
        if next_position_char() == "#":
            tree_count += 1

    print(f"{tree_count=}")
