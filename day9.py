# Problem: https://adventofcode.com/2020/day/9
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1(in_data, lag_size):
    n = len(in_data)
    for sum_pos in range(lag_size,n):
        if check_sum(in_data, sum_pos, lag_size) is False:
            return in_data[sum_pos]
    return -1


def check_sum(in_data, sum_pos, lag_size):
    for i in range(sum_pos-lag_size, sum_pos-1):
        for j in range(i+1, sum_pos):
            if in_data[i] + in_data[j] == in_data[sum_pos]:
                return True
    return False


def part2(in_data, bad_number):  # 23761694.0
    n = len(in_data)
    for i in range(n):
        sums = in_data[i]
        for j in range(i+1, n):
            if sums == bad_number:
                print(i,j)
                return min(in_data[i:j]) + max(in_data[i:j])
            sums += in_data[j]
    return -2


if __name__=='__main__':
    lag_size = 25
    in_filename = r'data\day9_in.txt'
    # in_filename = r'data\test9.txt'
    in_data = np.loadtxt(in_filename, dtype=float, delimiter='\n')
    bad_number = part1(in_data, lag_size)
    print('Part 1 solution: ' + str(bad_number))
    print('Part 2 solution: ' + str(part2(in_data, bad_number)))
