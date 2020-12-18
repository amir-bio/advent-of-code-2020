with open('./input.txt') as file:
    total_count = 0
    group_answer = set()
    for line in file:
        if line == "\n":
            print(f"{group_answer=}")
            total_count += len(group_answer)
            group_answer = set()
        else:
            print(f"{line=}")
            group_answer.update(*list(line.strip()))
    total_count += len(group_answer)
    print(f"Part 1: {total_count=}")

with open('./input.txt') as file:
    total_count = 0
    group_answer = None
    for line in file:
        if line == "\n":
            total_count += len(group_answer)
            print(f"{group_answer=} {total_count=}")
            group_answer = None
        else:
            if group_answer is not None:
                # there's already a group answer, take intersection
                print(f"existing group {line=}")
                group_answer = group_answer & set(list(line.strip()))
            else:
                print(f"new group {line=}")

                # there's no group answer, initialise g answer to first set
                group_answer = set(list(line.strip()))
    total_count += len(group_answer)
    print(f"Part 2: {total_count=}")
