# Problem: https://adventofcode.com/2020/day/2
# Date: December 2020
# Author: Alex Nazareth

import numpy as np


def part1():
    in_filename = 'day2_in.txt'

    in_data = np.loadtxt(in_filename, dtype=str)

    count_valid=0
    for p in in_data:
        countl=0
        minfr, maxfr = [int(m) for m in p[0].split('-')]
        letter = p[1].strip(':')
        for l in p[2]:
            if l==letter:
                countl += 1
                if countl>maxfr:
                    break
        if countl >= minfr and countl<=maxfr:
            count_valid += 1
    return(count_valid)


def part2():
    in_filename = 'day2_in.txt'

    in_data = np.loadtxt(in_filename, dtype=str)

    count_valid=0
    for p in in_data:
        countl=0
        pos1, pos2 = [int(m)-1 for m in p[0].split('-')]
        letter = p[1].strip(':')
        pword = p[2]
        if not((pword[pos1] == letter) == (pword[pos2] == letter)):
            count_valid += 1
    return(count_valid)


if __name__=='__main__':
    print(part2())