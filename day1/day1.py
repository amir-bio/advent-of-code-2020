"""
Part 1 Algorithm: Make a set of all input and then for each number, x, look up if 2020-x exists. If it exists return their
product.

Time complexity O(n)

NOTE: this solution doesn't work for the edge case where the number and its complement are the same
i.e. 1010 in this case - to support that need to ensure in that case there are 2 instances of 1010 in the original set
"""
from typing import Set, Tuple, Union

def find_pair_sum_to(values: Set[int], sum: int) -> Union[Tuple[int, int], None]:
    """Given a set of values and a sum, find a pair in set that add up to the sum. Returns None if no pair is found"""
    for number in values:
        complement = sum - number
        if complement in values:
            return (number, complement)
    return None


with open('./input.txt') as file:
    input: Set[int] = set([int(line.strip()) for line in file.readlines()])
    ans = find_pair_sum_to(input, 2020)
    if ans:
        a, b = ans
        print(f"Part 1: Found {a} and {b}, their product is: {a * b}")


"""
Part 2 Algorithm: Goal is to reduce this problem to previous problem - for any number,x, find a pair that adds up to
2020-x. To find a pair that adds up to 2020-x, reuse the previous part's solution.

Time complexity O(n)

NOTE: this solution doesn't work for the edge case where the number and its complement are the same
i.e. 1010 in this case - to support that need to ensure in that case there are 2 instances of 1010 in the original set
"""

with open('./input.txt') as file:
    input: Set[int] = set([int(line.strip()) for line in file.readlines()])
    for number in input:
        complement  = 2020 - number
        ans = find_pair_sum_to(input, complement)
        if ans:
            a, b = ans
            print(f"Part 2: Found {number} and {a} and {b}, their product is: {number * a * b}")
