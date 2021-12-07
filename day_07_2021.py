from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


"""
I tried several different ways: Center of mass, Average and Median
"""
@solution_timer(2021, 7, 1)
def part_one(input_data: List[str]):
    answer = None

    #input_data = ['16,1,2,0,4,2,7,1,2,14']
    data = [int(x) for x in input_data[0].split(',')]
    data.sort()
    #print(data)
    data_len = len(data)
    print('len=', data_len)

    median_value = data[int(data_len/2)]
    print('median=', median_value)

    avg_value = int(sum([x for x in data]) / data_len)
    print('avg=', avg_value)

    dict_of_mass = {}
    for x in data:
        if x in dict_of_mass:
            dict_of_mass[x] += 1
        else:
            dict_of_mass[x] = 1

    #print(dict_of_mass)

    data_sum = sum([(x*dict_of_mass[x]) for x in data])
    #print('sum=', data_sum)

    center_of_mass = data_sum // sum([m for m in dict_of_mass.values()])
    print('com=', center_of_mass)

    d_to_com = []
    for x in data:
        d_to_com.append(abs(center_of_mass-x))

    #print(d_to_com)
    print('sum2 using COM=', sum(d_to_com))

    d_to_avg = []
    for x in data:
        d_to_avg.append(abs(avg_value-x))
    print('sum3 using average=', sum(d_to_avg))


    d_to_median = []
    for x in data:
        d_to_median.append(abs(median_value-x))
    print('sum4 using median=', sum(d_to_median))

    answer = min([sum(d_to_com), sum(d_to_avg), sum(d_to_median)])

    if not answer:
        raise SolutionNotFoundException(2021, 7, 1)

    return answer

def gaussian_sum(n):
    # (n * (n + 1)) / 2 => (n^2 + n) / 2
    res = int((n**2 + n) / 2)
    return res

"""
I tried several different ways: Median, Average and used different functions to round up or down
"""
@solution_timer(2021, 7, 2)
def part_two(input_data: List[str]):
    import math
    answer = ...
    
    #input_data = ['16,1,2,0,4,2,7,1,2,14']
    
    data = [int(x) for x in input_data[0].split(',')]
    data.sort()

    median_value = data[int(len(data)/2)]
    print('median=', median_value)

    cost_med = sum([gaussian_sum(abs(median_value-x)) for x in data])
    print('cost median_value=', cost_med)


    avg1 = round(sum(data) / len(data)) #round works for test input round(2.5) = 2 roound(2.6) = 3
    cost1 = sum([gaussian_sum(abs(avg1-x)) for x in data])
    print('cost1=', cost1)

    # Gaussian sum: (n * (n + 1)) / 2 = 1+2+3+4+5+6 = 21 for n=6

    # use floor
    avg2 = math.floor(sum(data) / len(data))  # math.floor(2.6) = 2
    cost2 = sum([gaussian_sum(abs(avg2-x)) for x in data])
    print('cost2=', cost2)

    # user ceil
    avg3 = math.floor(sum(data) / len(data))  # math.ceil(2.1) = 3
    cost3 = sum([gaussian_sum(abs(avg3-x)) for x in data])
    print('cost3=', cost3)

    answer = min(cost1, cost2, cost3, cost_med)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 7)
    part_one(data)
    part_two(data)
