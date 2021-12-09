from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

def parse_input(input):
    res = []
    for _ in range(len(input)):
        res.append([]) 
    for i, row in enumerate(input):
        res[i].extend(int(x) for x in row)
    
    #print(res)
    return res

class HeightMap:
    def __init__(self, map_input):
        self.map = map_input
        self.risk_points = {}
        self.nrows = len(map_input)
        self.ncols = len(map_input[0])

    def check_depth(self, i, j):
        risk = 0
        res = (False, risk)
        val = self.map[i][j]
        #print('val=',val)
        if val == 9:
            return res
        nb = self.get_neighbours(i, j)
        _nb = [x for x in nb if x is not None]
        #print(_nb)
        _min = min(_nb)
        if val < _min:
            risk = 1 + val
            res = (True, risk)
            self.risk_points[(i,j)] = risk
        return res


    def get_neighbours(self, i, j):
        left = j-1 if j > 0 else None
        right = j+1 if j < (self.ncols-1) else None
        up = i-1 if i > 0 else None
        down = i+1 if i < (self.nrows-1) else None
        return [
            self.map[i][left] if left is not None else None, 
            self.map[i][right] if right is not None else None, 
            self.map[up][j] if up is not None else None, 
            self.map[down][j] if down is not None else None
        ]

    def get_sum_risk_levels(self):
        res = sum(self.risk_points.values())
        return res

    def get_neighbour_coords(self, i, j):
        left = j-1 if j > 0 else None
        right = j+1 if j < (self.ncols-1) else None
        up = i-1 if i > 0 else None
        down = i+1 if i < (self.nrows-1) else None
        return [
            (i, left) if left is not None else None, 
            (i, right) if right is not None else None, 
            (up, j) if up is not None else None, 
            (down, j) if down is not None else None
        ]

    def get_val_at(self, x):
        return self.map[x[0]][x[1]]


@solution_timer(2021, 9, 1)
def part_one(input_data: List[str]):
    answer = ...

    # input_data = [
    #     '2199943210',
    #     '3987894921',
    #     '9856789892',
    #     '8767896789',
    #     '9899965678']

    heightmap = HeightMap(parse_input(input_data))

    i = 0
    for _ in range(heightmap.nrows):
        j = 0
        for _ in range(heightmap.ncols):
            #print(i,j)
            res = heightmap.check_depth(i,j)
            #print(res)
            j += 1
        i += 1
    
    #print(heightmap.risk_points)

    answer = heightmap.get_sum_risk_levels()

    if not answer:
        raise SolutionNotFoundException(2021, 9, 1)

    return answer



@solution_timer(2021, 9, 2)
def part_two(input_data: List[str]):
    answer = ...

    # input_data = [
    #     '2199943210',
    #     '3987894921',
    #     '9856789892',
    #     '8767896789',
    #     '9899965678']

    heightmap = HeightMap(parse_input(input_data))

    i = 0
    for _ in range(heightmap.nrows):
        j = 0
        for _ in range(heightmap.ncols):
            #print(i,j)
            res = heightmap.check_depth(i,j)
            #print(res)
            j += 1
        i += 1
    
    #print(heightmap.risk_points)

    answer = heightmap.get_sum_risk_levels()

    # start from the lower locations
    sizes = []
    for i, j in heightmap.risk_points.keys():
        to_check = set()
        to_check.add((i,j))
        res = heightmap.get_neighbour_coords(i,j)
        for c in res:
            #print(c)
            to_check.add(c) if (c is not None) and heightmap.get_val_at(c) != 9 else _
        #print('to_check:', to_check)

        to_add = set()
        last_size = 0
        while True:
            last_size = len(to_check)
            for c in to_check:
                res = [x for x in heightmap.get_neighbour_coords(*c) if (x is not None) and heightmap.get_val_at(x) != 9]
                for x in res:
                    to_add.add(x)
                #print(res)
            for x in to_add:
                to_check.add(x)
            to_add.clear()
            if len(to_check) == last_size:
                break
            #print('to_add=', to_add)
        #print('to_check:', to_check, 'size = ', len(to_check))
        sizes.append(len(to_check))

    sizes.sort(reverse=True)
    #print(sizes)
    answer = sizes[0]*sizes[1]*sizes[2]

    if not answer:
        raise SolutionNotFoundException(2021, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 9)
    part_one(data)
    part_two(data)
