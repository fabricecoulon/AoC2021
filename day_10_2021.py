from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import deque

class ParsingError(Exception):
    pass

def process_line(l):
    return [c for c in l]

class Line:
    OPENS = ['(', '[', '{', '<']
    CLOSES = [')', ']', '}', '>']
    points = [3, 57, 1197, 25137]
    points_autocomplete = [1, 2, 3, 4]

    def __init__(self, lineno, l):
        self.lineno = lineno
        self.input_line_ls = l
        self.stack = deque()
        self.illegal_closing_char = ''
        self.completing = []

    def get_idx_of(self, c):
        idx = -1
        if c in self.OPENS:
            idx = self.OPENS.index(c)
        else:
            idx = self.CLOSES.index(c)
        return idx

    def check(self):
        for c in self.input_line_ls:
            if c in self.OPENS:
                self.stack.append(c)
            elif c in self.CLOSES:
                _pop = self.stack.pop()
                _pop_idx = self.get_idx_of(_pop)
                if (_pop_idx == self.get_idx_of(c)):
                    continue
                else:
                    self.illegal_closing_char = c
                    raise ParsingError('Got: ' + c + ' Expected: ' + self.CLOSES[_pop_idx])
        #print(self.stack)

    def do_complete(self):
        i = len(self.stack)-1
        reversed = []
        for _ in range(len(self.stack)):
            openc = self.stack[i]
            reversed.append(openc)  # contains opening brackets
            closec =  self.CLOSES[self.get_idx_of(openc)]
            self.completing.append(closec)
            i -= 1
        #print(self.completing)

    def get_completion_score(self):
        tot = 0
        for x in self.completing:
            tot = (tot*5) + self.points_autocomplete[self.get_idx_of(x)]
        return tot

@solution_timer(2021, 10, 1)
def part_one(input_data: List[str]):
    answer = None

#     input_data = [
# '[({(<(())[]>[[{[]{<()<>>',
# '[(()[<>])]({[<{<<[]>>(',
# '{([(<{}[<>[]}>{[]{[(<()>',
# '(((({<>}<{<{<>}{[]{[]{}',
# '[[<[([]))<([[{}[[()]]]',
# '[{[{({}]{}}([{[{{{}}([]',
# '{<[[]]>}<{[{[{[]{()[[[]',
# '[<(<(<(<{}))><([]([]()',
# '<{([([[(<>()){}]>(<<{{',
# '<{([{{}}[<[[[<>{}]]]>[]]']


    total_points = []
    i = 0
    for l in input_data:
        i += 1
        line = Line(i, l)
        try:
            line.check()
        except ParsingError as e:
            idx = Line.CLOSES.index(line.illegal_closing_char)
            total_points.append(Line.points[idx])
            #print('line ', i, e)
            continue


    answer = sum(total_points)

    if not answer:
        raise SolutionNotFoundException(2021, 10, 1)

    return answer


@solution_timer(2021, 10, 2)
def part_two(input_data: List[str]):
    answer = None

#     input_data = [
# '[({(<(())[]>[[{[]{<()<>>',
# '[(()[<>])]({[<{<<[]>>(',
# '{([(<{}[<>[]}>{[]{[(<()>',
# '(((({<>}<{<{<>}{[]{[]{}',
# '[[<[([]))<([[{}[[()]]]',
# '[{[{({}]{}}([{[{{{}}([]',
# '{<[[]]>}<{[{[{[]{()[[[]',
# '[<(<(<(<{}))><([]([]()',
# '<{([([[(<>()){}]>(<<{{',
# '<{([{{}}[<[[[<>{}]]]>[]]']


    total_points = []
    i = 0
    lineno_to_discard = []
    incomplete_lines = []
    for l in input_data:
        i += 1
        line = Line(i, l)
        try:
            line.check()
            incomplete_lines.append(line)
        except ParsingError as e:
            idx = Line.CLOSES.index(line.illegal_closing_char)
            total_points.append(Line.points[idx])
            #print('line ', i, e)
            lineno_to_discard.append(line.lineno)  # lineno 1-indexed
            continue

    all_scores = []
    for l in incomplete_lines:
        #print(l.input_line_ls , l.stack)
        l.do_complete()
        score = l.get_completion_score()
        #print(score)
        all_scores.append(score)

    all_scores.sort()
    import math
    middle = math.ceil(len(all_scores)/2)
    #print(all_scores)
    #print(middle)
    answer = all_scores[middle-1]

    if not answer:
        raise SolutionNotFoundException(2021, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 10)
    part_one(data)
    part_two(data)
