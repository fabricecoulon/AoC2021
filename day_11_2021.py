from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class Grid:
    def __init__(self, input_list_of_rows):
        self.grid = []
        self.nrows = len(input_list_of_rows)
        self.ncols = len(input_list_of_rows[0])
        for _ in range(self.ncols):
            self.grid.append([])
        for i, l in enumerate(input_list_of_rows):
            self.grid[i].extend([int(x) for x in l])
        #print(self.grid)
        self.nflash = 0



    def get_neighbours(self, i, j):
        if not (i >= 0 and i < self.nrows):
            raise Exception('i not in range')
        if not (j >= 0 and j < self.ncols):
            raise Exception('j not in range')
        left = (i, j-1) if j > 0 else None
        right = (i, j+1) if j < (self.ncols-1) else None
        up = (i-1, j) if i > 0 else None
        leftup = (i-1, j-1) if j>0 and i>0 else None
        rightup = (i-1, j+1) if i>0 and j < (self.ncols-1) else None
        down = (i+1, j) if i < (self.nrows-1) else None
        leftdown = (i+1, j-1) if (j>0) and i < (self.nrows-1) else None
        rightdown = (i+1, j+1) if i<(self.nrows-1) and j<(self.ncols-1) else None
        return [
            leftup, up, rightup, left, right, leftdown, down, rightdown
        ]

    def step(self, i):
        to_do = []  # keep track of those that need to be checked
        to_skip = []  # keep track of those that already flashed
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.grid[i][j] += 1
                if self.grid[i][j] > 9:
                    for _r, _c in [x for x in self.get_neighbours(i, j) if x is not None]:
                        to_do.append((_r, _c))
                    self.grid[i][j] = 0
                    self.nflash += 1
                    to_skip.append((i,j))

        while to_do:
            i, j = to_do.pop()
            if (i, j) in to_skip:
                continue
            self.grid[i][j] += 1
            if self.grid[i][j] > 9:
                for _r, _c in [x for x in self.get_neighbours(i, j) if x is not None]:
                    to_do.append((_r, _c))
                self.grid[i][j] = 0
                self.nflash += 1
                to_skip.append((i, j))

    def is_simultaneous(self):
        res = False
        tot = 0
        for i in range(self.nrows):
            if sum(self.grid[i]) == 0:
                tot += 1   
        return (tot == self.nrows)

@solution_timer(2021, 11, 1)
def part_one(input_data: List[str]):
    answer = ...

#     input_data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

#     input_data = """11111
# 19991
# 19191
# 19991
# 11111"""

    #grid = Grid(input_data.splitlines()) 
    grid = Grid(input_data) 

    _step = 0
    print('initial values at step', _step)
    for i, v in enumerate(grid.grid):
        print(v)
    while _step < 100:
        _step += 1
        grid.step(_step)
        print('after step ', _step)
        for i, v in enumerate(grid.grid):
            print(v)
        print('nflash=', grid.nflash)
    
    answer = grid.nflash

    if not answer:
        raise SolutionNotFoundException(2021, 11, 1)

    return answer


@solution_timer(2021, 11, 2)
def part_two(input_data: List[str]):
    answer = ...


#     input_data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

#     input_data = """11111
# 19991
# 19191
# 19991
# 11111"""

    #grid = Grid(input_data.splitlines()) 
    grid = Grid(input_data) 

    _step = 0
    print('initial values at step', _step)
    for i, v in enumerate(grid.grid):
        print(v)
    #while _step < 195:
    while not grid.is_simultaneous():
        _step += 1
        grid.step(_step)
        print('after step ', _step)
        for i, v in enumerate(grid.grid):
            print(v)
        print('step: ', _step, 'nflash=', grid.nflash, ' all flash = ', grid.is_simultaneous())
    
    answer = _step

    if not answer:
        raise SolutionNotFoundException(2021, 11, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 11)
    part_one(data)
    part_two(data)
