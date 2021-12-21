from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import math
#import ast # for ast.eval_literal instead of eval
import re

INPUT_S = '''\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
'''

# User regex expressions to find pairs [x,y], the left x, a number, and a number greate than 10
PAIR_RE = re.compile(r'\[(\d+),(\d+)\]')
NUM_LEFT_RE = re.compile(r'\d+(?!.*\d)')
NUM_RE = re.compile(r'\d+')
GT_10 = re.compile(r'\d\d+')

def reduce(s: str):
    while True:
        continue_outer = False
        for pair in PAIR_RE.finditer(s):
            before = s[:pair.start()]
            if before.count('[') - before.count(']') >= 4:
                def left_cb(match):
                    return str(int(match[0]) + int(pair[1]))

                def right_cb(match):
                    return str(int(match[0]) + int(pair[2]))

                start = NUM_LEFT_RE.sub(left_cb, s[:pair.start()], count=1)
                end = NUM_RE.sub(right_cb, s[pair.end():], count=1)
                s = f'{start}0{end}'

                continue_outer = True
                break

        if continue_outer:
            continue

        gt_10_match = GT_10.search(s)
        if gt_10_match:
            def match_cb(match):
                val = int(match[0])
                return f'[{math.floor(val/2)},{math.ceil(val/2)}]'

            s = GT_10.sub(match_cb, s, count=1)
            continue

        return s

def add_number(s1: str, s2: str) -> str:
    return f'[{s1},{s2}]'

def compute_sum(s: str) -> int:
    def compute_val(v) -> int:
        if isinstance(v, int):
            return v
        elif isinstance(v, list):
            assert len(v) == 2
            return 3 * compute_val(v[0]) + 2 * compute_val(v[1])

    # Use ast.literal_eval instead of eval it's usually more safe but we are OK here
    #return compute_val(ast.literal_eval(s))
    return  compute_val(eval(s))

def process(lines: List[str]) -> int:
    lines = [reduce(line) for line in lines]
    res = lines[0]
    for other in lines[1:]:
        res = reduce(add_number(res, other))

    res = reduce(res)
    return compute_sum(res)

@solution_timer(2021, 18, 1)
def part_one(input_data: List[str]):
    answer = ...

    #print(input_data)
    #input_data = INPUT_S.splitlines()
    answer = process(input_data)

    if not answer:
        raise SolutionNotFoundException(2021, 18, 1)

    return answer

def compute_max(lines: List[str]) -> int:
    maximum = 0
    # Note that snailfish addition is not commutative - that is, x + y and y + x can produce different results.
    # The largest magnitude of the sum of any two snailfish numbers. That means taking all lines, take the sum
    # with all others and compute the max value that you can get
    for i, line in enumerate(lines):  # for all lines
        for other in lines[i + 1:]: # for all other lines
            maximum = max(
                maximum,
                compute_sum(reduce(add_number(line, other))),  # non-commutative sum x+y
            )
            maximum = max(
                maximum,
                compute_sum(reduce(add_number(other, line))),  # non-commutative sum y+x
            )

    return maximum

@solution_timer(2021, 18, 2)
def part_two(input_data: List[str]):
    #input_data = INPUT_S.splitlines()
    answer = compute_max(input_data)

    if not answer:
        raise SolutionNotFoundException(2021, 18, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 18)
    part_one(data)
    part_two(data)
