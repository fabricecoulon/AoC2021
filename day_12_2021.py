from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import defaultdict, deque


INPUT_1 = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

INPUT_2 = '''\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

@solution_timer(2021, 12, 1)
def part_one(input_data: List[str]):
    answer = ...


    #print(input_data)
    #input_data = INPUT_2.splitlines()

    # 'dr-of', 'dr-IJ', 'dr-yj', 'dr-sk', 'dr-VT',...
    # -> defaultdict(<class 'set'>, {'dr': {'sk', 'IJ', 'of', 'yj', 'PZ', 'VT'},...
    edges = defaultdict(set)  # default value is a set
    for line in input_data:
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)

    #print(edges)

    done = set()

    # all paths start in tthe 'start' cave
    todo = deque([('start',)])
    while todo:
        path = todo.popleft()
        if path[-1] == 'end':
            # all paths that has last cave as end
            done.add(path)
            continue

        for choice in edges[path[-1]]:
            if choice.isupper() or (choice not in path):
                # it's a big cave (can be visited multiple times) or we haven't visited this before
                todo.append((*path,) + (choice,)) 

    #print(done)
    print(len(done))  # 4691
    
    answer = len(done)


    if not answer:
        raise SolutionNotFoundException(2021, 12, 1)

    return answer


@solution_timer(2021, 12, 2)
def part_two(input_data: List[str]):
    answer = ...

    #input_data = INPUT_2.splitlines()

    edges = defaultdict(set)  # default value is a set
    for line in input_data:
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)

    #print(edges)

    done = set()

    """
    a single small cave can be visited at most twice, and the remaining small caves can be visited at most once
    """

    # all paths start in tthe 'start' cave
    todo = deque([ (('start',), False ) ])
    while todo:
        path, at_most_twice = todo.popleft()
        if path[-1] == 'end':
            # all paths that has last cave as end
            done.add(path)
            continue

        #However, the caves named start and end can only be visited exactly once each:
        for choice in edges[path[-1]] - {'start'}:
            # it's a big cave
            if choice.isupper():
                todo.append( ((*path,) + (choice,), at_most_twice) ) 
            # a single small cave can be visited at most twice
            elif at_most_twice is False and path.count(choice) == 1:
                todo.append( ((*path,) + (choice,), True) )
            elif (choice not in path):
                # we haven't visited this before
                todo.append( ((*path,) + (choice,), at_most_twice) ) 

    #print(done)
    print(len(done))
    
    answer = len(done)

    if not answer:
        raise SolutionNotFoundException(2021, 12, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 12)
    #part_one(data)
    part_two(data)
