from typing import List, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import Counter

def get_scanners(input_data):
    scanners = []
    scanid = -1
    for raw_scanner in input_data:
        if raw_scanner.startswith('---'):
            scanners.append([])
            scanid += 1
            continue
        elif raw_scanner == '':
            continue
        scans_coords = [int(d) for d in raw_scanner.strip().split(',')]
        scanners[scanid].append(scans_coords)

    return scanners

"""
The scanners and beacons map a single contiguous 3d region. This region can be reconstructed by finding pairs of scanners that have overlapping detection regions 
such that there are at least 12 beacons that both scanners detect within the overlap. By establishing 12 common beacons, you can precisely determine where the scanners 
are relative to each other, allowing you to reconstruct the beacon map one scanner at a time.
"""
def check_if_scanners_overlap(scanners, base: int, to_check: int) -> Tuple[List[int], List[Tuple[int, int]]]:
    """
    Check if two scanners overlap (have 12+ beacons in common)
    1. We can check this one "direction" at a time as there are no beacons with duplicate x, y, or z coordinates
    2. We can assume that the base scanner (0) is aligned at X, Y, Z (whatever its alignment is, well just call it X, Y, Z)
    3. The other scanner will be aligned at a random combo of [X, -X, Y, -Y, Z, -Z] (24 options)
    Once we find a direction where we have 12 common, we've found our scanner and know its orientation and offset
    If they overlap, offsets, and orientations will not be empty
    """
    offsets, orientation = [], []
    base_scanner = scanners[base]
    scanner_to_check = scanners[to_check]

    # the base scanner is aligned at X, Y, Z => Column [0, 1, 2]
    # We want to find the offset and the orientation of the pair scanner in all 3 dirs
    for base_i in range(3):

        # the scanner to check, can have any combination of [X, -X, Y, -Y, Z, -Z]
        # we check one orientation/direction at a time (X = (1,0) -Y = (-1, 1) etc.)
        for sign, dir in [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, 2), (-1, 2)]:

            # get all the diffs/offsets between the base and ALL the possible orientations/directions of the check_scanner
            diffs = [beacon0[base_i] - sign * beacon1[dir]
                     for beacon1 in scanner_to_check
                     for beacon0 in base_scanner]

            # if we have 12+ matched in any direction, we have found our pair scanner
            # and we know the offset, and also the orientation/direction of this column
            offset, matching_beacons = Counter(diffs).most_common()[0]

            if matching_beacons >= 12:
                offsets.append(offset)
                orientation.append((sign, dir))

    return offsets, orientation

def find_overlapping(scanners, scannerid: int, to_check: List[int]) -> Tuple[int, List[int], List[Tuple[int, int]]]:
    for other_scanner in to_check:
        offsets, orientation = check_if_scanners_overlap(scanners, scannerid, other_scanner)
        if len(offsets) > 0:
            return other_scanner, offsets, orientation
    return -1, [], []

"""
Modify the scanners list with the found orientation
"""
def align_scanner(scanners, scanner, offsets, orientation):
    to_align = scanners[scanner]

    # align orientation
    sign0, col0 = orientation[0]
    sign1, col1 = orientation[1]
    sign2, col2 = orientation[2]
    to_align = [[sign0 * beacon[col0], sign1 * beacon[col1], sign2 * beacon[col2]] for beacon in to_align]

    # align offset
    to_align = [[beacon[0] + offsets[0], beacon[1] + offsets[1], beacon[2] + offsets[2]] for beacon in to_align]

    scanners[scanner] = to_align

def align_scanners(scanners):
    aligned_scanners = [0]
    un_aligned_scanners = [i for i in range(1, len(scanners))]

    all_offsets = []

    while un_aligned_scanners:
        for i in aligned_scanners:
            overlapping_scanner, offsets, orientation = find_overlapping(scanners, i, un_aligned_scanners)
            if overlapping_scanner != -1:
                #print("Found overlapping scanners:", i, overlapping_scanner, offsets, orientation)
                align_scanner(scanners, overlapping_scanner, offsets, orientation)
                un_aligned_scanners.remove(overlapping_scanner)
                aligned_scanners.append(overlapping_scanner)
                all_offsets.append(offsets)

    return all_offsets


TEST_INPUT = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""

def count_beacons(scanners):
    unique_beacons = set()

    for scanner in scanners:
        for beacon in scanner:
            unique_beacons.add((beacon[0], beacon[1], beacon[2]))
    
    # To check with the list of 79 beacons found in the puzzle description:
    #_sorted = list(unique_beacons)
    #_sorted.sort(key=lambda val: val[0])
    #print(_sorted)

    return len(unique_beacons)

@solution_timer(2021, 19, 1)
def part_one(input_data: List[str]):
    answer = None

    # To test with the test data from the puzzle description:
    #input_data = TEST_INPUT.splitlines()
    #print(input_data)
    #print(get_scanners(input_data)[0])
    scanners = get_scanners(input_data)
    #print(scanners[0])
    offsets = align_scanners(scanners)
    answer = count_beacons(scanners)

    if not answer:
        raise SolutionNotFoundException(2021, 19, 1)

    return answer

def get_biggest_manhattan_distance(offsets) -> int:
    biggest_distance = 0

    for i in range(len(offsets)):
        for j in range(i + 1, len(offsets)):
            manhattan = abs(offsets[i][0] - offsets[j][0]) + abs(offsets[i][1] - offsets[j][1]) + abs(offsets[i][2] - offsets[j][2])
            biggest_distance = max(biggest_distance, manhattan)

    return biggest_distance

@solution_timer(2021, 19, 2)
def part_two(input_data: List[str]):
    answer = None

    scanners = get_scanners(input_data)
    #print(scanners[0])
    offsets = align_scanners(scanners)    
    answer = get_biggest_manhattan_distance(offsets)

    if not answer:
        raise SolutionNotFoundException(2021, 19, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 19)
    part_one(data)
    part_two(data)
