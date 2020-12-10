# Problem: https://adventofcode.com/2020/day/10
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1(in_data):
    in_data = in_data.sort()
    diff_dict = {1: 0, 2: 0, 3: 0}
    prev_joltage = in_data[0]
    for curr_joltage in in_data[1:]:
        diff_dict[curr_joltage - prev_joltage] += 1
        prev_joltage = curr_joltage
    return diff_dict[1]*diff_dict[3]


def part2(in_data):
    return -2


if __name__=='__main__':
    # in_filename = r'data\day10_in.txt'
    in_filename = r'data\test10.txt'
    in_data = np.loadtxt(in_filename, dtype=int, delimiter='\n')

    print(part1(in_data))