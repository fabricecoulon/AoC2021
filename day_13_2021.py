from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

input1 = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

class Grid:
    def __init__(self, maxx, maxy, inputs=None):
        self.grid = []
        self.nrows = maxy
        self.ncols = maxx
        for _ in range(self.nrows):
            self.grid.append([0 for _ in range(self.ncols)])

        """ The first value, x, increases to the right (grid cols). The second value, y, increases downward (grid rows) """
        if inputs is not None:
            for x, y in inputs:
                self.grid[y][x] = 1

    def fold_along_y(self, at_y):
        _newgrid = Grid(self.ncols, at_y)
        crow = 0
        #print('---')
        for y in range(self.nrows-1, at_y, -1):
            _newgrid.grid[crow] = self.merge(self.grid[crow], self.grid[y])
            #print(_newgrid.grid[crow])
            crow += 1
        return _newgrid

    def fold_along_x(self, at_x):
        _newgrid = Grid(at_x, self.nrows)

        #print('---')
        # self.ncols-1, at_x, -1
        for i in range(self.nrows):
            #print(1, self.grid[i][0:at_x])
            #print(2, self.grid[i][at_x+1:self.ncols][::-1])
            _newgrid.grid[i] = self.merge(self.grid[i][0:at_x], self.grid[i][at_x+1:self.ncols][::-1])
            #print(_newgrid.grid[i])
        return _newgrid

    def merge(self, l1, l2):
        res = [0 for _ in l1]
        for i, x in enumerate(l1):
            res[i] = l1[i] + l2[i]
            if res[i] > 1:
                res[i] = 1
        return res

    def nb_of_dots(self):
        tot = 0
        for i in range(self.nrows):
            tot += sum(self.grid[i])
        return tot

@solution_timer(2021, 13, 1)
def part_one(input_data: List[str]):
    answer = None

    max_x = 0
    max_y = 0
    fold_instructions = []
    #input_data = input1.splitlines()
    inputs = []
    for l in input_data:
        if l == "":
            continue
        elif l.startswith('fold'):
            _fold = l.split(' ')
            fold_instructions.append(_fold[2])
            continue
        # transform x,y to Python tuples (x, y)
        _tuple = eval("(" + l + ")")
        x, y = _tuple
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        inputs.append(_tuple)
    #print(inputs)
    #print(fold_instructions)

    grid = Grid(max_x + 1 , max_y + 1, inputs)

    for foldi in fold_instructions:
        at, pos = foldi.split('=')
        print(at, pos)
        if at == 'y':
            grid = grid.fold_along_y(int(pos))
        elif at == 'x':
            grid = grid.fold_along_x(int(pos))
        break # after the FIRST fold (17)

    answer = grid.nb_of_dots()

    if not answer:
        raise SolutionNotFoundException(2021, 13, 1)

    return answer


@solution_timer(2021, 13, 2)
def part_two(input_data: List[str]):
    answer = None

    max_x = 0
    max_y = 0
    fold_instructions = []
    #input_data = input1.splitlines()
    inputs = []
    for l in input_data:
        if l == "":
            continue
        elif l.startswith('fold'):
            _fold = l.split(' ')
            fold_instructions.append(_fold[2])
            continue
        # transform x,y to Python tuples (x, y)
        _tuple = eval("(" + l + ")")
        x, y = _tuple
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        inputs.append(_tuple)
    #print(inputs)
    #print(fold_instructions)

    grid = Grid(max_x + 1 , max_y + 1, inputs)

    for foldi in fold_instructions:
        at, pos = foldi.split('=')
        #print(at, pos)
        if at == 'y':
            grid = grid.fold_along_y(int(pos))
        elif at == 'x':
            grid = grid.fold_along_x(int(pos))

    for i in range(grid.nrows):
        #print(grid.grid[i])
        lcode = ''
        for j in range(grid.ncols):
            lcode += '#' if grid.grid[i][j] == 1 else ' '
        if lcode:
            print(i, lcode)

    if not answer:
        raise SolutionNotFoundException(2021, 13, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 13)
    part_one(data)
    part_two(data)  # ECFHLHZF
