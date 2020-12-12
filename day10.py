# Problem: https://adventofcode.com/2020/day/10
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1(in_data):
    in_data = np.sort(in_data)
    # initial joltage diff from source is 1, and final diff to my device is 3
    diff_dict = {1: 1, 2: 0, 3: 1}
    prev_joltage = in_data[0]
    for curr_joltage in in_data[1:]:
        diff_dict[curr_joltage - prev_joltage] += 1
        prev_joltage = curr_joltage
    return diff_dict[1]*diff_dict[3]


def part2(in_data):
    in_data = np.hstack((0, np.sort(in_data)))
    in_data = np.append(in_data, in_data[-1]+3)
    n = len(in_data)
    return num_possibilities(in_data, 0, n, dict())


def num_possibilities(in_data, posn, n, visited):
    if posn == n-1:
        return 1
    else:
        max_njpos = min(posn+4, n)
        cj = in_data[posn]  # current joltage
        poss_njpos = [njpos for njpos in range(posn+1, max_njpos) \
                        if in_data[njpos]-cj <= 3]
        result = 0
        for njpos in poss_njpos:
            if njpos in visited:
                result += visited[njpos]
            else:
                temp = num_possibilities(in_data, njpos, n, visited)
                visited[njpos] = temp
                result += temp
        return result


if __name__=='__main__':
    in_filename = r'data\day10_in.txt'
    in_data = np.loadtxt(in_filename, dtype=int, delimiter='\n')
    print('Part 1 solution: ' + str(part1(in_data)))
    print('Part 2 solution: ' + str(part2(in_data)))