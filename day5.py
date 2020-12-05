# Problem: https://adventofcode.com/2020/day/5
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1():
    in_filename = r'data\day5_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str)

    max_seat_id = -1
    for bp in in_data:
        temp_id = get_row(bp)*8 + get_col(bp)
        max_seat_id = max(temp_id, max_seat_id)
    print(max_seat_id)


def part2():
    in_filename = r'data\day5_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str)

    id_list = []
    for bp in in_data:
        id_list.append(get_row(bp)*8 + get_col(bp))

    id_list.sort()
    for i in range(1,len(id_list)):
        if id_list[i]-id_list[i-1]==2:
            result = id_list[i]-1
            break
    print(result)

        
def get_row(boarding_pass):
    row_a, row_b = 0, 128
    for l in boarding_pass[0:7]:
        if l=='F':
            row_b = row_a + (row_b-row_a)/2
        elif l=='B':
            row_a = row_a + (row_b-row_a)/2
        else:
            print('invalid input, expected F or B, got: ' + l)
    return row_a


def get_col(boarding_pass):
    col_a, col_b = 0, 8
    for l in boarding_pass[7:10]:
        if l=='L':
            col_b = col_a + (col_b-col_a)/2
        elif l=='R':
            col_a = col_a + (col_b-col_a)/2
        else:
            print('invalid input, expected L or R, got: ' + l)
    return col_a


if __name__=='__main__':
    part2()