# Problem: https://adventofcode.com/2020/day/6
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re

def part1():
    in_filename = r'data\day6_in.txt'
    with open(in_filename) as f:
        group_list = []
        group_str = ''
        count=0
        for line in f.readlines():
            if line=='\n':
                group_list.append(group_str)
                count += len(set(group_str.strip(' ')))
                group_str = ''
            else:
                group_str = group_str + line.strip('\n')
        count += len(set(group_str.strip(' ')))
    print(count)


def part2():
    in_filename = r'data\day6_in.txt'
    with open(in_filename) as f:
        count=0
        common_answers = {}
        for line in f.readlines():
            if line=='\n':
                count += len(common_answers)
                common_answers={}
            elif common_answers == {}:
                common_answers = set(line.strip('\n'))
            else:
                common_answers = common_answers.intersection(set(line.strip('\n')))
        count += len(common_answers)
    print(count)


if __name__=='__main__':
    part1()
    part2()