from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class BingoBoard:
    bbid = 1
    def __init__(self, size=5, data=None):
        self.id = BingoBoard.bbid
        BingoBoard.bbid += 1
        self.size = size
        self.rows = []
        self.match_by_rows = []
        self.match_by_rows.extend([0 for _ in range(self.size)])
        self.match_by_columns = []
        self.match_by_columns.extend([0 for _ in range(self.size)])
        self.marked = []
        for _ in range(self.size):
            self.rows.append([])
            self.marked.append([])
        for i in range(5):
            self.rows[i].extend([0 for _ in range(self.size)])
            self.marked[i].extend([0 for _ in range(self.size)])

        if data is not None:
            if data == []:
                raise RuntimeError
            self.init_with_data(data)

    def init_with_data(self, data):
        assert len(data) == self.size
        for i in range(self.size):
            _inputrow = [int(x) for x in data[i].split(' ') if x != '']
            #print(_inputrow)
            self.rows[i].clear()
            self.rows[i].extend(_inputrow)     
            #self.rows[i].extend() 

    def __str__(self):
        res = ""
        res += '-- id# ' + str(self.id) + ' --\n'
        for i in range(self.size):
            res += ' '.join((str(x)  for x in self.rows[i]))
            res += ' => ' + str(self.match_by_rows[i])
            res += '\n'
        res += '-'*10 + '\n'
        res += ' '.join((str(x) for x in self.match_by_columns))
        return res

    def process_input(self, val):
        res = False
        # print(_input_nb)
        i = 0 # idx row
        j = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.rows[i][j] == val:
                    self.match_by_rows[i] += 1
                    self.match_by_columns[j] += 1
                    self.marked[i][j] = 1

        for i in self.match_by_rows:
             if i == self.size:
                 res = True
                 break

        for i in self.match_by_columns:
             if i == self.size:
                 res = True
                 break
        
        return res

    def get_sum_of_unmarked(self):
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.marked[i][j] == 0:  # unmarked numbers
                    sum += self.rows[i][j]
        return sum

@solution_timer(2021, 4, 1)
def part_one(input_data: List[str]):
    answer = None

    #print(input_data)

    first_line = input_data[0]
    #print(first_line)
    first_line_as_ls = [int(x) for x in first_line.split(',') if x != '']
    #print(first_line_as_ls)
    bingo_grids = input_data[2:]
    bingo_grids_filtered = [x for x in bingo_grids if x != '']
    assert len(bingo_grids_filtered) % 5 == 0
    #print(bingo_grids_filtered)
    #print('bg1 = ', bingo_grid1)

    #print(input_data)
    bingo_boards = []
    bb_idx = 0
    while True:
        _bingo_grid = bingo_grids_filtered[(0+(bb_idx*5)):(5+(bb_idx*5))]
        if _bingo_grid == []:
            break
        bb = BingoBoard(5, _bingo_grid)
        bingo_boards.append(bb)
        bb_idx += 1

    # for bb in bingo_boards:
    #     print(bb)
    #     print("="*20)

    win = False
    for x in first_line_as_ls:
        for bb in bingo_boards:
            win = bb.process_input(x)
            if win:
                print(bb)
                _sum = bb.get_sum_of_unmarked()
                print('get_sum_of_unmarked: ', _sum)
                answer = _sum * x
                break
        if win:
            break


    if not answer:
        raise SolutionNotFoundException(2021, 4, 1)

    return answer


@solution_timer(2021, 4, 2)
def part_two(input_data: List[str]):
    answer = None

    #print(input_data)

    first_line = input_data[0]
    #print(first_line)
    first_line_as_ls = [int(x) for x in first_line.split(',') if x != '']
    #print(first_line_as_ls)
    bingo_grids = input_data[2:]
    bingo_grids_filtered = [x for x in bingo_grids if x != '']
    assert len(bingo_grids_filtered) % 5 == 0
    #print(bingo_grids_filtered)
    #print('bg1 = ', bingo_grid1)

    #print(input_data)
    bingo_boards = []
    bb_idx = 0
    while True:
        _bingo_grid = bingo_grids_filtered[(0+(bb_idx*5)):(5+(bb_idx*5))]
        if _bingo_grid == []:
            break
        bb = BingoBoard(5, _bingo_grid)
        bingo_boards.append(bb)
        bb_idx += 1

    # for bb in bingo_boards:
    #     print(bb)
    #     print("="*20)

    win = False
    to_remove = []
    last_answer = 0
    for x in first_line_as_ls:
        for bb in bingo_boards:
            win = bb.process_input(x)
            if win:
                print(bb)
                _sum = bb.get_sum_of_unmarked()
                print('get_sum_of_unmarked: ', _sum)
                last_answer = _sum * x
                print('answer = ', last_answer)
                to_remove.append(bb)
        for bb in to_remove:
            bingo_boards.remove(bb)
        to_remove.clear()
        if len(bingo_boards) == 0:
            answer = last_answer

    if not answer:
        raise SolutionNotFoundException(2021, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 4)
    #part_one(data)
    part_two(data)
