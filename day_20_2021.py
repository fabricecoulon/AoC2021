from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import defaultdict

"""
The first section is the image enhancement algorithm. It is normally given on a single line.
The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).
"""

INPUT_S = '''\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''


def read_input(input_data):
    algorithm, image_lines = input_data[0], input_data[1:]

    image = defaultdict(lambda: "0")

    for row, line in enumerate(image_lines):
        for col, c in enumerate(line):
            if c == "#":
                image[(col, row)] = "1"   # cols are x (width), rows are y (height)

    return algorithm, image, len(image_lines[0]), len(image_lines)

def print_image(image, width, height):
    for y in range(height):
        print(''.join([ image[(x, y)] for x in range(width) ]))

def print_image2(image, minx, maxx, miny, maxy):
    for y in range(miny, maxy):
        print("".join([ '#' if image[(x, y)] == "1" else '.' for x in range(minx, maxx) ]))



def enhance_image(image, algorithm, minx, maxx, miny, maxy):
    new_image = defaultdict(lambda: "0")

    for y in range(miny + 1, maxy):
        for x in range(minx + 1, maxx):
            binary = "".join(image[(dx, dy)] for dy in range(y - 1, y + 2) for dx in range(x - 1, x + 2))
            if algorithm[int(binary, 2)] == "#":
                new_image[(x, y)] = "1"

    return new_image

def flip_outer_rim(image, minx, maxx, miny, maxy, n):
    value = "0" if n % 2 else "1"
    for y in range(miny, maxy + 1):
        image[(minx, y)] = value
        image[(maxx, y)] = value
    for x in range(minx, maxx + 1):
        image[(x, miny)] = value
        image[(x, maxy)] = value
    return image

def run_enhancements(image, width, height, algorithm, steps, debug=True):
    padding = 2 * steps

    # pad the image (with all 0s) - enough layers to cover all the steps
    minx, miny = 0 - padding, 0 - padding
    maxx, maxy = width + padding, height + padding

    for step in range(steps):
        if debug:
            print("--- STEP #{} ---".format(step))
            print("\nbefore\n")
            #print_image(image, width, height)
            print_image2(image, minx, maxx, miny, maxy)
        image = enhance_image(image, algorithm, minx, maxx, miny, maxy)
        if debug:
            print("\nafter\n")
            print_image2(image, minx, maxx, miny, maxy)
        # The layer corresponds to zero or one, depending on the parity of the iteration,
        # to account for the fact that item zero in the algorithm is "#" (not in the example INPUT_S but in the puzzle input!!)
        image = flip_outer_rim(image, minx, maxx, miny, maxy, step)

    return image, sum(1 for c in image.values() if c == "1")

@solution_timer(2021, 20, 1)
def part_one(input_data: List[str]):
    answer = ...

    #input_data = [l for l in INPUT_S.splitlines() if l != ""]
    input_data = [x for x in input_data if x != ""]
    algo, img, width, height = read_input(input_data)

    #print_image(img, width, height)
    img, num_lit = run_enhancements(img, width, height, algo, 2)

    answer = num_lit

    if not answer:
        raise SolutionNotFoundException(2021, 20, 1)

    return answer


@solution_timer(2021, 20, 2)
def part_two(input_data: List[str]):
    answer = ...

    input_data = [x for x in input_data if x != ""]
    algo, img, width, height = read_input(input_data)

    #print_image(img, width, height)
    img, num_lit = run_enhancements(img, width, height, algo, 50, False)

    answer = num_lit

    if not answer:
        raise SolutionNotFoundException(2021, 20, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 20)
    part_one(data)
    part_two(data)
