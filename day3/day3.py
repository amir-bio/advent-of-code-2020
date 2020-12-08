def part1_solution(dx, dy):
    tree_count = 0
    x = y = 0

    def next_position_char() -> str:
        nonlocal x, y
        x += dx
        y += dy
        return input_grid[y][x % original_grid_width]

    while y < original_grid_height - 1:
        if next_position_char() == "#":
            tree_count += 1
    return tree_count


with open('./input.txt') as file:
    # list of lines, each line represent one row
    input_grid = [line.strip() for line in file]
    original_grid_height = len(input_grid)
    original_grid_width = len(input_grid[0])

    print(f"Part 1: {part1_solution(3, 1)}")
    print(
        f"Part 2: {part1_solution(1, 1) * part1_solution(3, 1) * part1_solution(5, 1) * part1_solution(7, 1) * part1_solution(1, 2)}")
