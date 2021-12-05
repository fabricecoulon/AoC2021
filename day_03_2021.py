from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

class StatusReport:
    def __init__(self):
        #per_bitcol
        self.nb_bitcol = 0
        self.nb_of_ones = []
        self.nb_of_zeros = []
        self.gamma_rate = []
        self.epsilon_rate = []
    
    def set_nb_bitcol(self, val):
        self.nb_bitcol = val
        #print(self.nb_bitcol)
        for x in range(self.nb_bitcol):
            self.nb_of_ones.append(0)
            self.nb_of_zeros.append(0)
            self.gamma_rate.append(0)
            self.epsilon_rate.append(0)
        #print(self.nb_of_ones)
        #print(self.nb_of_zeros)

    def __str__(self):
        return "1: {} 0: {}".format(self.nb_of_ones, self.nb_of_zeros)

    def process_data(self, data):
        for pos, val in enumerate(data):
            match val:
                case '1':
                    self.nb_of_ones[pos] += 1
                case '0':
                    self.nb_of_zeros[pos] += 1
                case _:
                    raise NotImplementedError

    def calc_gamma_and_epsilon(self):
        for i in range(self.nb_bitcol):
            if self.nb_of_ones[i] > self.nb_of_zeros[i]:
                self.gamma_rate[i] = '1'
            elif self.nb_of_zeros[i] > self.nb_of_ones[i]:
                self.epsilon_rate[i] = '1'
            else:
                raise NotImplementedError


    def get_gamma_rate_as_str(self):
        """ Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report """
        return ''.join(str(i) for i in self.gamma_rate)

    def get_gamma_rate(self):
        return int(self.get_gamma_rate_as_str(), 2)

    def get_epsilon_rate_as_str(self):
        return ''.join(str(i) for i in self.epsilon_rate)

    def get_epsilon_rate(self):
        return int(self.get_epsilon_rate_as_str(), 2)

    def get_power_consumption(self):
        return (self.get_gamma_rate() * self.get_epsilon_rate())

@solution_timer(2021, 3, 1)
def part_one(input_data: List[str]):
    answer = None

    #print(input_data)

    # String binary to int
    #print(int('10110', 2))
    #print(int('01001', 2))

    sr = StatusReport()
    sr.set_nb_bitcol(len(input_data[0]))
    for i in input_data:
        #print(i)
        sr.process_data(i)
        #print(sr)

    sr.calc_gamma_and_epsilon()
    print(sr.get_gamma_rate_as_str(), "=>", sr.get_gamma_rate())
    print(sr.get_epsilon_rate_as_str(), "=>", sr.get_epsilon_rate())
    answer = sr.get_power_consumption()

    if not answer:
        raise SolutionNotFoundException(2021, 3, 1)

    return answer

# ==========================================================================


class StatusReportPart2:
    def __init__(self, input_data):
        #per_bitcol
        self.nb_of_ones = []
        self.nb_of_zeros = []
        self.set_nb_bitcol(len(input_data[0]))

    def reset(self, new_input_data):
        self.nb_of_ones.clear()
        self.nb_of_zeros.clear()
        self.set_nb_bitcol(len(new_input_data[0]))

    def set_nb_bitcol(self, val):
        self.nb_bitcol = val
        #print(self.nb_bitcol)
        for x in range(self.nb_bitcol):
            self.nb_of_ones.append(0)
            self.nb_of_zeros.append(0)

    def __str__(self):
        return "1: {} 0: {}".format(self.nb_of_ones, self.nb_of_zeros)

    def process_data(self, data):
        for pos, val in enumerate(data):
            match val:
                case '1':
                    self.nb_of_ones[pos] += 1
                case '0':
                    self.nb_of_zeros[pos] += 1
                case _:
                    raise NotImplementedError

    # get_oxygen_genrating
    """
    most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    """
    def most_common_val(self, pos):
        res = None
        for x in range(self.nb_bitcol):
            if self.nb_of_ones[pos] > self.nb_of_zeros[pos]:
                res = '1'
            elif self.nb_of_zeros[pos] > self.nb_of_ones[pos]:
                res = '0'
            else:
                res = '1'
        return res

    def least_common_val(self, pos):
        res = None
        for x in range(self.nb_bitcol):
            if self.nb_of_ones[pos] > self.nb_of_zeros[pos]:
                res = '0'
            elif self.nb_of_zeros[pos] > self.nb_of_ones[pos]:
                res = '1'
            else:
                res = '0'
        return res

    def analyze_o2(self, input_data):
        inputd = input_data[:]
        x = 0
        output = []
        while len(inputd) != 1:
            self.reset(inputd)
            for i in inputd:
                self.process_data(i)
            output.clear()
            mcv = self.most_common_val(x)
            #lcv = self.least_common_val(x)
            for data in inputd:
                if data[x] == mcv:
                    output.append(data)
            #print(output)
            x += 1
            inputd = output[:]

        #print(int(inputd[0], 2))
        return int(inputd[0], 2)


    def analyze_co2(self, input_data):
        inputd = input_data[:]
        x = 0
        output = []
        while len(inputd) != 1:
            self.reset(inputd)
            for i in inputd:
                self.process_data(i)
            output.clear()
            lcv = self.least_common_val(x)
            for data in inputd:
                if data[x] == lcv:
                    output.append(data)
            #print(output)
            x += 1
            inputd = output[:]

        #print(int(inputd[0], 2))
        return int(inputd[0], 2)

@solution_timer(2021, 3, 2)
def part_two(input_data: List[str]):
    answer = None

    sr = StatusReportPart2(input_data)
    #sr.set_nb_bitcol(len(input_data[0]))
    o2 = sr.analyze_o2(input_data)
    #print(o2)
    co2 = sr.analyze_co2(input_data)
    #print(co2)
    # print('most common val at 0 = ', sr.most_common_val(0))
    # print('least common val at 0 = ', sr.least_common_val(0))    

    # print('most common val at 1 = ', sr.most_common_val(1))
    # print('least common val at 1 = ', sr.least_common_val(1))

    answer = o2 * co2

    if not answer:
        raise SolutionNotFoundException(2021, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 3)
    part_one(data)
    part_two(data)
