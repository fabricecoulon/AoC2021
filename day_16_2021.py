from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from dataclasses import dataclass

@dataclass
class Packet:
    version: int = -1
    type_id: int = -1
    n: int = -1
    packets: tuple = ()

class BinStringWithPos:
    def __init__(self, hex):
        self.position = 0
        self.bin_str = ''
        for c in hex:
            self.bin_str += f'{int(c, 16):04b}'  # Convert to 4 bits binary string repr
        #print(self.bin_str)

    def read(self, nbits):
        _begin = self.position
        _end = self.position + nbits
        res = self.bin_str[_begin:_end]
        self.position += nbits
        return res

def parse_packet(bin_str):
    """ 
    Read n bits and move read position inside the bin_str
    """
    #print('parsing packet at pos = ', bin_str.position)
    def _read(nbits):
        return int(bin_str.read(nbits), 2)

    version = _read(3)
    type_id = _read(3)

    if type_id == 4:
        n = 0
        # literal
        chunk = _read(5)
        n += chunk & 0b1111
        while chunk & 0b10000:
            chunk = _read(5)
            n <<= 4
            n += chunk & 0b1111

        return bin_str.position, Packet(version=version, type_id=type_id, n=n)
    else:
        mode = _read(1)

        if mode == 0:
            bits_length = _read(15)
            _begin = bin_str.position
            _end = bin_str.position + bits_length
            packets = []
            while _begin < _end:
                _begin, packet = parse_packet(bin_str)
                packets.append(packet)

            ret = Packet(
                version=version,
                type_id=type_id,
                packets=tuple(packets),
            )
            return bin_str.position, ret
        else:
            sub_packets = _read(11)
            packets = []
            for _ in range(sub_packets):
                _, packet = parse_packet(bin_str)
                packets.append(packet)
            ret = Packet(
                version=version,
                type_id=type_id,
                packets=tuple(packets),
            )
            return bin_str.position, ret

def calculate_value(packet):
    if packet.type_id == 0:
        return sum(calculate_value(sub_packet) for sub_packet in packet.packets)
    elif packet.type_id == 1:
        res = 1
        for sub_packet in packet.packets:
            res *= calculate_value(sub_packet)
        return res
    elif packet.type_id == 2:
        return min(calculate_value(sub_packet) for sub_packet in packet.packets)
    elif packet.type_id == 3:
        return max(calculate_value(sub_packet) for sub_packet in packet.packets)
    elif packet.type_id == 4:
        return packet.n
    elif packet.type_id == 5:
        return calculate_value(packet.packets[0]) > calculate_value(packet.packets[1])
    elif packet.type_id == 6:
        return calculate_value(packet.packets[0]) < calculate_value(packet.packets[1])
    elif packet.type_id == 7:
        return calculate_value(packet.packets[0]) == calculate_value(packet.packets[1])
    else:
        raise


@solution_timer(2021, 16, 1)
def part_one(input_data: List[str]):
    answer = None

    total = 0
    for hex in input_data:
        bin_str = BinStringWithPos(hex)
        _, packet = parse_packet(bin_str)  # starts recursively parsing packets from position 0 in the bin_str
        todo = [packet]
        while todo:
            item = todo.pop()
            total += item.version
            todo.extend(item.packets)

    answer = total

    if not answer:
        raise SolutionNotFoundException(2021, 16, 1)

    return answer


@solution_timer(2021, 16, 2)
def part_two(input_data: List[str]):
    answer = None

    total = 0
    for hex in input_data:
        bin_str = BinStringWithPos(hex)
        _, packet = parse_packet(bin_str)  # starts recursively parsing packets from position 0 in the bin_str
        todo = [packet]
        while todo:
            item = todo.pop()
            todo.extend(item.packets)
        total += calculate_value(packet)

    answer = total

    if not answer:
        raise SolutionNotFoundException(2021, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 16)
    part_one(data)  #991
    part_two(data) #1264485568252
