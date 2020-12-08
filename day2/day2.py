# Part 1
valid_pws = 0
with open('./input.txt') as file:
    lines = [line.strip() for line in file]
    for line in lines:
        # sample line: "5-7 s: swsskgwsbzv"
        rule, pw = line.split(':')
        pw = pw.strip() # remove left whitespace
        number_range, char = rule.split(' ')
        start, end = number_range.split('-')
        valid_pws += int(start)<= pw.count(char) <= int(end)

print("part 1 valid passwords:" , valid_pws)

# Part 2
valid_pws = 0
with open('./input.txt') as file:
    lines = [line.strip() for line in file]
    for line in lines:
        # sample line: "5-7 s: swsskgwsbzv"
        rule, pw = line.split(':')
        pw = pw.strip() # remove left whitespace
        position_pair, char = rule.split(' ')
        first_position, second_position = position_pair.split('-')
        # essentially an xor of the 2 booleans
        valid_pws += (pw[int(first_position)-1] == char) != (pw[int(second_position)-1] == char)

print("part 2 valid passwords:" , valid_pws)
