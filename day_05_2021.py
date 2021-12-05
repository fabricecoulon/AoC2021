from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

def get_line_start_and_end_coordinates(line):
    start = eval("[" + line[:line.index(" ")] + "]")
    end = eval("[" + line[line.index(">")+2:] + "]")
    return [[start, end]]

def step_points(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    if dx != 0:
        dx = dx // abs(dx)
    if dy != 0:
        dy = dy // abs(dy)
    while start[0] != end[0] or start[1] != end[1]:
        yield start
        start[0] += dx
        start[1] += dy
    yield end

def gen_key(point):
    # 000|000 ...
    return f'{point[0]:03}|{point[1]:03}'

@solution_timer(2021, 5, 1)
def part_one(input_data: List[str]):
    answer = None
    #print(input_data)
    pts = {}  # key = key_string => nb times it occured
    for line in input_data:
        d = get_line_start_and_end_coordinates(line)
        for start,end in d:
            #print(start, end)
            # !!! Consider ONLY horizontal and vertical lines
            if start[0] == end[0] or start[1] == end[1]:
                for p in step_points(start, end):
                    #print(p)
                    _key = gen_key(p)
                    pts[_key] = pts.get(_key, 0) + 1
    s = sum([1 if v > 1 else 0 for v in pts.values()])
    answer = s

    if not answer:
        raise SolutionNotFoundException(2021, 5, 1)

    return answer


@solution_timer(2021, 5, 2)
def part_two(input_data: List[str]):
    answer = None
    #print(input_data)
    pts = {}  # key = key_string => nb times it occured
    for line in input_data:
        d = get_line_start_and_end_coordinates(line)
        for start,end in d:
            #print(start, end)
            # !!! Consider ALL lines !!!
            for p in step_points(start, end):
                #print(p)
                _key = gen_key(p)
                pts[_key] = pts.get(_key, 0) + 1
    s = sum([1 if v > 1 else 0 for v in pts.values()])
    answer = s

    if not answer:
        raise SolutionNotFoundException(2021, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 5)
    part_one(data)
    part_two(data)
