# Problem: https://adventofcode.com/2020/day/15
# Date: December 2020
# Author: Alex Nazareth


import numpy as np


def part1(start_nums, end_num):
    num_list = [int(s) for s in start_nums]
    last_said = {s: i for i, s in enumerate(num_list[:-1])}
    for i in range(len(num_list), end_num):
        last_num = num_list[-1]
        if last_num not in last_said:
            last_said[last_num] = i-1
            num_list.append(0)
        else:
            diff = i - 1 - last_said[last_num]
            last_said[last_num] = i-1
            num_list.append(diff)
    return num_list[-1]


def part2():
    return -2


if __name__ == '__main__':
    test_input = '6,3,15,13,1,0'.split(',')  # actual test inpyt
    # test_input = '2,3,1'.split(',')  # practice
    print(part1(test_input, 2020))
