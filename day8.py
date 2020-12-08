# Problem: https://adventofcode.com/2020/day/8
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1():
    in_filename = r'data\day8_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')

    instr_counter = np.zeros(len(in_data), dtype=int)
    acc = 0
    cmd_pos = 0
    while True:
        # print(str(cmd_pos) + ' - ' + str(acc))
        if instr_counter[cmd_pos]>0:
            return acc
        instr_counter[cmd_pos] += 1
        cmd = in_data[cmd_pos][0:3]
        if cmd == 'acc':
            acc += int(in_data[cmd_pos][3:])
            cmd_pos += 1
        elif cmd == 'jmp':
            cmd_pos += int(in_data[cmd_pos][3:])
        else:
            cmd_pos += 1


def part2():




if __name__=='__main__':
    print(part1())