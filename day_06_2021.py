from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

def parse_input1(astring):
    res = [int(x) for x in astring.split(',')]
    return res

def parse_input2(astring):
    fishesd = {}
    for k in [int(i) for i in astring.split(',')]:
        if k in fishesd:
            fishesd[k] += 1
        else:
            fishesd[k] = 1
    return fishesd

"""
This was just to produce a nice output to verify the logic during the first steps :-)
"""
def process_data1(ilist):
    ilistcpy = ilist[:]
    to_add = []
    for i, x in enumerate(ilistcpy):
        match x:
            case 0:
                ilist[i] = 6
                to_add.append(8)                
                continue
        ilist[i] = ilist[i] - 1

    if to_add:
        for _ in to_add:
            ilist.append(8)
        to_add.clear()

    return ilist

"""
Use a dictionary to keep track of the nb of fishes in every gen/stages
"""
def process_data2(data):
    data_next = {}
    to_add = 0
    for k in data.keys():
        if k == 0:
            # all 0 become 6
            if 6 in data_next:
                data_next[6] += data[k]
            else:
                data_next[6] = data[k]
            # and append one to 8 for each 6
            to_add += data[k]
            continue

        if (k-1) in data_next:
            data_next[k-1] += data[k]
        else:
            data_next[k-1] = data[k]

    if to_add > 0:
        if 8 in data_next:
            data_next[8] += to_add
        else:
            data_next[8] = to_add

    return data_next



@solution_timer(2021, 6, 1)
def part_one(ndays, input_data: List[str]):
    answer = None

    #print(ndays)

    #input_data = ['3,4,3,1,2']
    #print(input_data)
    data = parse_input2(input_data[0])
    #print(data)
    #print("day {}: {} len={}".format(0, data, sum(data.values())))

    i = 0
    while i < ndays:
        data = process_data2(data)
        _sum = sum(data.values())        
        #print("day {}: {} len={}".format(i+1, data, _sum))
        if (i == (ndays-1)):
            print("day {}: len={}".format(i+1, _sum))
        i += 1

    answer = _sum

    if not answer:
        raise SolutionNotFoundException(2021, 6, 1)

    return answer




@solution_timer(2021, 6, 2)
def part_two(ndays, input_data: List[str]):
    answer = None

    data = parse_input2(input_data[0])

    i = 0
    while i < ndays:
        data = process_data2(data)
        _sum = sum(data.values())        
        #print("day {}: {} len={}".format(i+1, data, _sum))
        if (i == (ndays-1)):
            print("day {}: len={}".format(i+1, _sum))
        i += 1

    answer = _sum

    if not answer:
        raise SolutionNotFoundException(2021, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 6)
    ndays = 80
    part_one(ndays, data)
    ndays = 256
    part_two(ndays, data)
