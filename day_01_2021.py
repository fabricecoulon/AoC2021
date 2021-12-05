"""
watchmedo shell-command --patterns="day_01_2021.py" --command 'python day_01_2021.py' --drop
"""
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 1, 1)
def part_one(input_data: List[str]):
    answer = None

    lastx = -1
    nbTimesInc = 0
    for x in [int(e) for e in input_data]:
        if lastx == -1:
           #print("{} (N/A - no previous measurement)".format(x))
           pass
        elif x > lastx:
            #print("{} (increased)".format(x))
            nbTimesInc += 1
        elif x < lastx:
            #print("{} (decreased)".format(x))
            pass 
        lastx = x

    print("nbTimesInc = ", nbTimesInc)

    answer = nbTimesInc

    if not answer:
        raise SolutionNotFoundException(2021, 1, 1)

    return answer

"""
@solution_timer(2021, 1, 2)
def part_two(input_data: List[str]):
    data = [int(e) for e in input_data]
    #answer =sum([1 for i, x in enumerate(data[3:]) if x > data[i]])

    def count_increases(depths: List[int]) -> int:
        increases = [1 for first, second in zip(depths, depths[1:]) if second > first]
        return len(increases)


    def count_sliding_increases(depths: List[int]) -> int:
        sliding_sums = [
            sum(measurements) for measurements in zip(depths, depths[1:], depths[2:])
        ]
        return count_increases(sliding_sums)

    answer = count_sliding_increases(data)

    if not answer:
        raise SolutionNotFoundException(2021, 1, 2)

    return answer
"""

@solution_timer(2021, 1, 2)
def part_two(input_data: List[str]):
    #data = [int(e) for e in input_data]

    slice0 = [int(e) for e in input_data]
    slice1 = slice0[1:]
    slice2 = slice0[2:]

    #print(slice0)
    #print(slice1)
    #print(slice2)

    w1 = []
    w2 = []
    last_sum = -1
    i = 0
    windows=[]
    try:
        for x in slice0:
            w1 = [slice0[i], slice1[i], slice2[i]]
            windows.append(w1)
            #print(i, " : ", w1)
            i += 1
    except IndexError as e:
        #print('No more data')
        pass

    #print(windows)

    last_sum = -1
    i = 0
    nbTimesInc = 0
    for x in windows:
        win_sum = sum(x)
        if last_sum == -1:
            #print("{}: {} (N/A - no previous sum)".format(i, win_sum))
            last_sum = win_sum
        else:
            if win_sum > last_sum:
                #print("{}: {} (increased)".format(i, win_sum))
                nbTimesInc += 1
            elif win_sum < last_sum:
                #print("{}: {} (decreased)".format(i, win_sum))
                pass
            elif win_sum == last_sum:
                #print("{}: {} (no change)".format(i, win_sum))
                pass
            last_sum = win_sum        
        i += 1

    answer = nbTimesInc

    if not answer:
        raise SolutionNotFoundException(2021, 1, 2)

    return answer

if __name__ == '__main__':
    import time
    data = get_input_for_day(2021, 1)
    #print(data)
    part_one(data)
    part_two(data)
    #time.sleep(1)
