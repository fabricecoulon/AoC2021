from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

class Position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def forward(self, x):
        self.horizontal += x

    def down(self, x):
        self.depth += x

    def up(self, x):
        self.depth -= x

    def __str__(self):
        return "h: {} d: {}".format(self.horizontal, self.depth)

class PositionPartTwo(Position):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def down(self, x):
        # I've misunderstood the problem: "entirely different!"
        #super().down(x)
        self.aim += x

    def up(self, x):
        # I've misunderstood the problem: "entirely different!"
        #super().up(x)
        self.aim -= x
    
    def forward(self, x):
        # forward is the same command
        super().forward(x)
        self.depth += (self.aim *x)

    def __str__(self) -> str:
        msg = super().__str__()
        msg += " a: {}".format(self.aim)
        return msg

def process_command(apos, acommand, aval):
    match acommand:
        case 'forward':
            apos.forward(aval)
        case 'down':
            apos.down(aval)
        case 'up':
            apos.up(aval)
        case _:
            raise NotImplementedError()

@solution_timer(2021, 2, 1)
def part_one(input_data: List[str]):
    answer = None

    current_position = Position()
    for l in input_data:
        [command, val] = l.split(' ')
        process_command(current_position, command, int(val))

    answer = current_position.horizontal * current_position.depth

    if not answer:
        raise SolutionNotFoundException(2021, 2, 1)

    return answer


@solution_timer(2021, 2, 2)
def part_two(input_data: List[str]):
    answer = None

    current_position = PositionPartTwo()
    for l in input_data:
        [command, val] = l.split(' ')
        #print(command, val)
        process_command(current_position, command, int(val))
        #print(str(current_position))

    answer = current_position.horizontal * current_position.depth

    if not answer:
        raise SolutionNotFoundException(2021, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 2)
    part_one(data)
    part_two(data)
