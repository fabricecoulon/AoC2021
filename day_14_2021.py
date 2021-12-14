import collections
from typing import Deque, List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

input1 = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def parse_line_into_key_val_pairs(line):
    key: str = eval("'" + line[:line.index(" ")] + "'")
    val: str = eval("'" + line[line.index(">")+2:] + "'")
    return (key.strip(), val.strip())

def process_polytpl(polytpl_ls, rules):
    res = ''
    complete = False
    while not complete:
        found = False
        i = 0
        for el in list(polytpl_ls):
            if len(polytpl_ls) == 1:
                res += ''.join(polytpl_ls)
                complete = True
                break
            two = polytpl_ls[0] + polytpl_ls[1]
            #print('two:',two)
            for k in rules.keys():
                if k == two:
                    res += polytpl_ls[0] + rules[k] #+ polytpl_ls[1]
                    found = True
                    polytpl_ls.popleft()
                    break
            if found:
                i += 2
                found = False
                break
        #print('res:',res)
    return res



@solution_timer(2021, 14, 1)
def part_one(input_data: List[str], niter=10):
    answer = None

    #lines = input1.splitlines()
    lines = input_data
    polytpl0 = lines[0].strip()
    rules: dict = {}
    for l in lines[1:]:
        if l.strip() == "":
            continue
        k, v = parse_line_into_key_val_pairs(l)
        rules[k] = v

    #print(rules)

    polytpl_ls = collections.deque(polytpl0)
    iter = 0
    print(iter, ':', polytpl_ls)
    while iter < niter:
        iter += 1
        res = process_polytpl(polytpl_ls, rules)
        print(iter, ':', res)
        polytpl_ls = collections.deque(res)

    poly_tot = {}
    for k in res:
        if k not in poly_tot:
            poly_tot[k] = 1
        else:
            poly_tot[k] += 1

    print(poly_tot)
    _sorted = sorted(poly_tot.items(), key=lambda x: int(x[1]), reverse=True)
    print(_sorted) #[('B', 1749), ('N', 865), ('C', 298), ('H', 161)]
      # max occurences value - min occurences value
    delta = _sorted[0][1] - _sorted[-1][1]
    print(delta)

    answer = len(res), res, delta

    if not answer:
        raise SolutionNotFoundException(2021, 14, 1)

    return answer


@solution_timer(2021, 14, 2)
def part_two(input_data: List[str], niter=40):
    answer = None

    lines = input_data
    polytpl0 = lines[0].strip()
    rules: dict = {}
    for l in lines[1:]:
        if l.strip() == "":
            continue
        k, v = parse_line_into_key_val_pairs(l)
        rules[k] = v

    # The trick to manage part 2 is to focus only on counting the occurences
    # not focus on building the result string as I did in part 1...
    def compute(s, patterns) -> int:
        counts = collections.Counter()
        for i in range(0, len(s) - 1):
            counts[s[i:i + 2]] += 1

        for _ in range(niter):
            counts2 = collections.Counter()
            new_counts = collections.Counter()
            for k, v in counts.items():
                new_counts[f'{k[0]}{patterns[k]}'] += v
                new_counts[f'{patterns[k]}{k[1]}'] += v
                counts2[k[0]] += v
                counts2[patterns[k]] += v
            counts = new_counts

        counts2[s[-1]] += 1

        s_counts = sorted(v for v in counts2.values())
        return (s_counts[-1] - s_counts[0])

    answer = compute(polytpl0, rules)

    if not answer:
        raise SolutionNotFoundException(2021, 14, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 14)
    part_one(data)
    part_two(data)
