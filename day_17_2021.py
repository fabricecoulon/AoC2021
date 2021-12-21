from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(input_data):
    _,_,_x,_y = input_data.split(' ')
    print(_x, _y)
    _xrange = _x.split('=')[1]
    _yrange = _y.split('=')[1]
    print(_xrange, _yrange)
    xmin, xmax = (int(x.replace(',','')) for x in _xrange.split('..'))
    ymin, ymax = (int(y) for y in _yrange.split('..'))
    print(xmin,xmax,ymin,ymax)
    return xmin, xmax, ymin, ymax

@solution_timer(2021, 17, 1)
def part_one(input_data: List[str]):
    answer = ...
    print(input_data)
    xmin, xmax, ymin, ymax = parse_input(input_data[0])

    # brute force:
    # ans = 0
    # for _dx in range(xmax+100):
    #     for _dy in range(ymin-100, ymin+1000):
    #         ok = False
    #         max_y = 0
    #         x = y = 0
    #         dx = _dx
    #         dy = _dy
    #         for t in range(1000):
    #             x += dx
    #             y += dy
    #             max_y = max(max_y,y)
    #             if dx > 0:
    #                 dx -= 1
    #             elif x < 0:
    #                 dx += 1
    #             dy -= 1
    #             if xmin <= x <= xmax and ymin <= y <= ymax:
    #                 ok = True
    #                 break
    #         if ok:
    #             if max_y > ans:
    #                 ans = max_y
    #                 print(_dx,_dy, ans)

    # math:
    # if you write the series for y it's a gaussian sum
    depth = abs(ymin)-1   # the length between y=0 and y=abs(ymin)
    answer = depth * (depth+1) // 2  # just the Gaussian sum

    if not answer:
        raise SolutionNotFoundException(2021, 17, 1)

    return answer


def probe(dx, dy, min_x, max_x, min_y, max_y):
    x, y = 0, 0

    while x <= max_x and y >= min_y:
        x += dx
        y += dy

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        dx = max(0, dx - 1)
        dy -= 1

    return False

@solution_timer(2021, 17, 2)
def part_two(input_data: List[str]):
    xmin, xmax, ymin, ymax = parse_input(input_data[0])
    # to find every initial velocity that causes the probe to eventually be within the target area after any step.
    answer =  sum(1 for x in range(xmax + 1) for y in range(ymin, abs(ymin) + 1) if probe(x, y, xmin, xmax, ymin, ymax))
    if not answer:
        raise SolutionNotFoundException(2021, 17, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 17)
    part_one(data)
    part_two(data)
