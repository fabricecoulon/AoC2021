from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

"""
heapq module provides an implementation of the heap queue algorithm, also known as the priority queue
algorithm. Heaps are binary trees for which every parent node has a value less than or equal to any of its
children. This implementation uses arrays for which heap[k] <= heap[2*k+1] and 
heap[k] <= heap[2*k+2] for all k, counting elements from zero.
Heap elements can be tuples.
This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:
>>>
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
"""
import heapq

INPUT_S = '''\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''

def get_all_coords(coords, input_data):
    for i, l in enumerate(input_data):
        for j in range(len(l)):
            coords[(i, j)] = int(l[j])

def compute(start, end, coords, best_at):
    _todo = [(0, start)]
    while len(_todo) != 0:
        _cost, _last_coord = heapq.heappop(_todo)

        if (_last_coord in best_at) and (_cost >= best_at[_last_coord]):
            continue
        else:
            best_at[_last_coord] = _cost
            #print(_last_coord, _cost)

        if _last_coord == end:
            return _cost

        for c in [ (_last_coord[0]-1, _last_coord[1]),
                   (_last_coord[0], _last_coord[1]-1),
                   (_last_coord[0]+1, _last_coord[1]),
                   (_last_coord[0], _last_coord[1]+1) ]:
            #print(c)
            if c in coords:
                heapq.heappush(_todo, (_cost + coords[c], c))
                #print('add: ', c)

    return best_at[end]

@solution_timer(2021, 15, 1)
def part_one(input_data: List[str]):
    answer = ...

    #input_data = INPUT_S.splitlines()
    #print(input_data)
    coords: dict[tuple(int, int)] = {}
    get_all_coords(coords, input_data)
    #print(coords)

    start = (0,0) # end = (maxx, maxy)
    end = max(coords)    
    best_at: dict[tuple[int, int], int] = {}
    res = compute(start, end, coords, best_at)
    print(res)
    answer = res

    if not answer:
        raise SolutionNotFoundException(2021, 15, 1)

    return answer


def five_times_larger(input_data):
    larger = []
    _len = len(input_data[0])
    for i, l in enumerate(input_data):
        new_l = [int(x) for x in l]
        for n in range(4):
            new_l += [ int(x)+1 if int(x)+1 <= 9 else 1 for x in new_l[(n*_len):(n*_len)+_len] ]
        larger.append(new_l)

    n = 0
    while n < 4:
        new_ls = []
        for l in larger[(n*_len):(n*_len)+_len]:
            new_ls.append([ int(x)+1 if int(x)+1 <= 9 else 1 for x in l ])
        larger.extend(new_ls)
        n += 1

    res = ''
    for i, l in enumerate(larger):
        res += ''.join([str(x) for x in l]) + '\n'

    return res

@solution_timer(2021, 15, 2)
def part_two(input_data: List[str]):
    answer = ...

    #input_data = INPUT_S.splitlines()
    larger_input_data = five_times_larger(input_data)

    #print(larger_input_data)

    answer = part_one(larger_input_data.splitlines())

    if not answer:
        raise SolutionNotFoundException(2021, 15, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 15)
    #part_one(data)
    part_two(data)
