# Problem: https://adventofcode.com/2020/day/1
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import time


def part1():
    in_filename = 'day1_in.txt'
    TARGET_SUM = 2020

    in_data = np.loadtxt(in_filename, dtype=int, delimiter='\n')

    for i in range(len(in_data)):
        for j in range(i+1,len(in_data)):
            if in_data[i] + in_data[j] == TARGET_SUM:
                return(in_data[i]*in_data[j])
    return(-1)


def part2():
    in_filename = 'day1_in.txt'
    TARGET_SUM = 2020

    in_data = np.loadtxt(in_filename, dtype=int, delimiter='\n')
    for i in in_data:
        for j in in_data:
            if i+j<2020:
                for k in in_data:
                    if sum((i,j,k))==TARGET_SUM:
                        return(i*j*k)
    return(-1)


if __name__=='__main__':
    tic = time.perf_counter()
    print(part2())
    toc = time.perf_counter()
    print(str(toc-tic) + 's')