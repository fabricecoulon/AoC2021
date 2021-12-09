from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

def parse_input_line(line, signals, outputs):
    signal, output = line.split("|")
    signals.append([s.strip() for s in signal.strip().split(" ")])
    outputs.append([o.strip() for o in output.strip().split(" ")])

@solution_timer(2021, 8, 1)
def part_one(input_data: List[str]):
    answer = ...

    signals = []
    outputs = []
    for l in input_data:
        parse_input_line(l, signals, outputs)
    print(signals)
    print(outputs)

    # digit 1: len = 2
    # digit 4: len = 4
    # digit 7: len = 3
    # digit 8: len = 7
    tot = 0
    for _output in outputs:
        for _o in _output:
           if len(_o) in [2,4,3,7]:
               tot += 1

    answer = tot 

    if not answer:
        raise SolutionNotFoundException(2021, 8, 1)

    return answer

def convert_to_binary_value_from_signal_value(value):
    mask = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    binary = ''.join(['1' if x in value else '0' for x in mask])
    return int(binary, 2)

# 5 bars
# 1 & x == 2 set, x = 3
# 4 & y == 2 set, y = 2
# z = 5

# 6 bars
# 1 & x = 1 set, x = 6
# 4 & y = 4 set, y = 9
# z = 0
def decode_signal(signal):
    # we already know these unique signal to digit display for digits '1', '4', '7' and '8'
    s1 = next(x for x in signal if len(x) == 2) # signal for digit '1'
    s4 = next(x for x in signal if len(x) == 4)
    s7 = next(x for x in signal if len(x) == 3)
    s8 = next(x for x in signal if len(x) == 7)

    # We have to deduce s2, s3, s5 (that have 5 bars) and s0, s6, s9 (that 6 letters/bars)
    for x in signal:
        if len(x) != 5:
            continue
        # convert to binary, do a bitwise AND then
        # count the number of ones in the binary representation to know if it is overlapping
        # with a '2', '3' or '5'. For example '1' and '3' have 2 bars overlapping.
        # '2' and '4' have 2 overlapping bars. '5' and '4' have 3 overlapping bars.
        if bin(convert_to_binary_value_from_signal_value(x) & convert_to_binary_value_from_signal_value(s1)).count('1') == 2:
            s3 = x
        elif bin(convert_to_binary_value_from_signal_value(x) & convert_to_binary_value_from_signal_value(s4)).count('1') == 2:
            s2 = x
        else:
            s5 = x
    
    for x in signal:
        if len(x) != 6:
            continue
        # '6' and '1' have 1 overlapping bars
        if bin(convert_to_binary_value_from_signal_value(x) & convert_to_binary_value_from_signal_value(s1)).count('1') == 1:
            s6 = x
        # '9' and '4' have 4 overlapping bars 
        elif bin(convert_to_binary_value_from_signal_value(x) & convert_to_binary_value_from_signal_value(s4)).count('1') == 4:
            s9 = x
        # only one left to deduce
        else:
            s0 = x

    return {s0: '0', s1: '1', s2: '2', s3: '3', s4: '4',
            s5: '5', s6: '6', s7: '7', s8: '8', s9: '9'}

def parse_output(output, decoded):
    return int(''.join([decoded[o] for o in output]))


@solution_timer(2021, 8, 2)
def part_two(input_data: List[str]):
    answer = None

    signals = []
    outputs = []
    for l in input_data:
        parse_input_line(l, signals, outputs)

    #print(signals)
    #print(outputs)

    all_digits = []
    for signal, output in zip(signals, outputs):
        signal = [''.join(sorted(x)) for x in signal]
        output = [''.join(sorted(x)) for x in output]
        #print('signal: ', signal)
        #print('output: ', output)
        decoded = decode_signal(signal)
        #print(decoded)
        all_digits.append(parse_output(output, decoded))
    
    answer = sum(all_digits)

    if not answer:
        raise SolutionNotFoundException(2021, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 8)
    part_one(data)
    part_two(data)
