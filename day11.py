# Problem: https://adventofcode.com/2020/day/11
# Date: December 2020
# Author: Alex Nazareth


import numpy as np
import re


def part1(in_data):
    seating_matrix = in_data.copy()
    prev_seating_matrix = None
    while True:
        seating_matrix, num_occupied = update_seating(seating_matrix)
        print(seating_matrix)
        if np.array_equal(prev_seating_matrix, seating_matrix):
            return num_occupied
        else:
            prev_seating_matrix = seating_matrix.copy()
    return -1

def update_seating(seating_matrix):
    updated_seating = seating_matrix.copy()
    num_occupied = 0
    for i in range(len(seating_matrix)):
        for j in range(len(seating_matrix[i])):
            if seating_matrix[i][j] == 'L' and \
                sum_adjacent(seating_matrix, i, j) == 0:  # if empty
                    updated_seating[i][j] = '#'
                    num_occupied += 1
            elif seating_matrix[i][j] == '#':
                if sum_adjacent(seating_matrix, i, j) >=4:
                    updated_seating[i][j] = 'L'  # person leaves seat
                else:
                    num_occupied += 1
    return updated_seating, num_occupied


def sum_adjacent(seating_matrix, i, j):
    sum_adj_occ = 0
    i_max = len(seating_matrix)
    j_max = len(seating_matrix[0])
    if i==0 and j==8:
        print('whats going on here')
    for x in range(max(i-1, 0), min(i+2, i_max)):
        for y in range(max(j-1, 0), min(j+2, j_max)):
            if seating_matrix[x][y] == '#' and (i!=x or j!=y):
                sum_adj_occ += 1
    return sum_adj_occ

    
def part2(in_data):
    return -2


if __name__=='__main__':
    in_filename = r'data\day11_in.txt'
    # in_filename = r'data\test11.txt'
    in_data = np.loadtxt(in_filename, dtype=str)
    in_data2 = np.array([list(r) for r in in_data])
    print(len(in_data2))
    print(len(in_data2[0]))
    print('Part 1 solution: ' + str(part1(in_data2)))
    # print('Part 2 solution: ' + str(part2(in_data)))