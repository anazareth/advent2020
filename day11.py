# Problem: https://adventofcode.com/2020/day/11
# Date: December 2020
# Author: Alex Nazareth


import numpy as np
import re


def part1(in_data):
    seating_matrix = in_data.copy()
    prev_seating_matrix = seating_matrix
    while True:
        seating_matrix, num_occupied = update_seating(seating_matrix)
        print(seating_matrix)
        if np.array_equal(prev_seating_matrix, seating_matrix):
            return num_occupied
        else:
            prev_seating_matrix = seating_matrix
    return -1

def update_seating(seating_matrix):
    updated_seating = seating_matrix.copy()
    num_occupied = 0
    for i in range(len(seating_matrix[0])):
        for j in range(len(seating_matrix[i])):
            if seating_matrix[i][j] == 'L':  # if empty
                if desirable_seat(seating_matrix, i, j, False):
                    updated_seating[i][j] = '#'
                    num_occupied += 1
            elif seating_matrix[i][j] == '#':  # if occupied
                if not desirable_seat(seating_matrix, i, j, True):
                    updated_seating[i][j] = 'L'
                else:
                    num_occupied += 1
    return updated_seating, num_occupied


def sum_adjacent(seating_matrix, i, j):
    sum_adj_occ = 0
    i_max = len(seating_matrix)-1
    j_max = len(seating_matrix[0])-1
    for x in range(max(i-1, 0), min(i+2, i_max)):
        for y in range(max(j-1, 0), min(j+2, j_max)):
            if seating_matrix[x][y] == '#' and (i!=x or j!=y):
                sum_adj_occ += 1
    return sum_adj_occ

# def desirable_seat(seating_matrix, i, j, occupied):
#     sum_adj_occ = 0
#     i_max = len(seating_matrix)-1
#     j_max = len(seating_matrix[0])-1
#     for x in range(max(i-1, 0), min(i+2, i_max)):
#         for y in range(max(j-1, 0), min(j+2, j_max)):
#             if seating_matrix[x][y] == '#' and (i!=x or j!=y):
#                 sum_adj_occ += 1
#                 if occupied:
#                     return False
#                 if not occupied and sum_adj_occ >= 4:
#                     return True
    return True

    
def part2(in_data):
    return -2


if __name__=='__main__':
    # in_filename = r'data\day11_in.txt'
    in_filename = r'data\test11.txt'
    in_data = np.loadtxt(in_filename, dtype=str)
    in_data2 = np.array([list(r) for r in in_data])
    print('Part 1 solution: ' + str(part1(in_data2)))
    # print('Part 2 solution: ' + str(part2(in_data)))