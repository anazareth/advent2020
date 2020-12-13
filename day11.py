# Problem: https://adventofcode.com/2020/day/11
# Date: December 2020
# Author: Alex Nazareth


import numpy as np
import re


EMPTY = 0
OCCUPIED = 1
FLOOR = -1


def part1(in_data):
    seating_matrix = in_data.copy()
    prev_seating_matrix = None
    while True:
        seating_matrix, num_occupied = update_seating(seating_matrix, 4)
        if np.array_equal(prev_seating_matrix, seating_matrix):
            return num_occupied
        else:
            prev_seating_matrix = seating_matrix.copy()
    return -1

    
def part2(in_data):
    seating_matrix = in_data.copy()
    prev_seating_matrix = None
    while True:
        seating_matrix, num_occupied = update_seating(seating_matrix, 5)
        print_seating_matrix(seating_matrix)
        if np.array_equal(prev_seating_matrix, seating_matrix):
            return num_occupied
        else:
            prev_seating_matrix = seating_matrix.copy()
    return -1


def update_seating(seating_matrix, adj_threshold):
    updated_seating = seating_matrix.copy()
    num_occupied = 0
    for i in range(len(seating_matrix)):
        for j in range(len(seating_matrix[i])):
            if seating_matrix[i][j] == EMPTY and \
                sum_adjacent_pt2(seating_matrix, 2, 3)==0:  # if empty
                    updated_seating[i][j] = OCCUPIED
                    num_occupied += 1
            elif seating_matrix[i][j] == OCCUPIED:
                if sum_adjacent_pt2(seating_matrix, i, j)>=5:
                    updated_seating[i][j] = EMPTY  # person leaves seat
                else:
                    num_occupied += 1
    return updated_seating, num_occupied


def sum_adjacent(seating_matrix, i, j, max_adj):
    sum_adj_occ = 0
    i_max = len(seating_matrix)
    j_max = len(seating_matrix[0])
    for x in range(max(i-1, 0), min(i+2, i_max)):
        for y in range(max(j-1, 0), min(j+2, j_max)):
            if seating_matrix[x][y] == OCCUPIED and (i!=x or j!=y):
                sum_adj_occ += 1
                if sum_adj_occ >= max_adj:
                    return True
    return False


def sum_adjacent_pt2(seating_matrix, i, j):
    sum_adj_occ = 0
    i_max = len(seating_matrix)
    j_max = len(seating_matrix[0])
    # print(i+1, i_max)
    for x in range(i+1, i_max): # downward direction
        if seating_matrix[x,j]==1:
            sum_adj_occ += 1
            break
    # print(0, i)
    for x in range(i-1, -1, -1): # upward direction
        if seating_matrix[x,j]==1:
            sum_adj_occ += 1
            break
    # print(range(j+1, j_max))
    for y in range(j+1, j_max): # right direction
        if seating_matrix[i,y]==1:
            sum_adj_occ += 1
            break
    # print(reversed(range(0, j)))
    for y in range(j-1, -1, -1): # left direction
        if seating_matrix[i,y]==1:
            sum_adj_occ += 1
            break
    # print(range(1, min(i_max-i, j_max-j)))
    for d in range(1, min(i_max-i, j_max-j)): # SE direction
        if seating_matrix[i+d,j+d]==1:
            sum_adj_occ += 1
            break
    # print(range(1, min(i+1-0, j+1-0)))
    for d in range(1, min(i-0, j-0)+1): # NW direction
        # print(i-d,j-d)
        if seating_matrix[i-d,j-d]==1:
            sum_adj_occ += 1
            break
    # print(range(1, min(i+1-0, j_max-j)))
    for d in range(1, min(i+1-0, j_max-j)): # NE direction
        if seating_matrix[i-d,j+d]==1:
            sum_adj_occ += 1
            break
    # print(range(1, min(i_max-i, j+1-0)))
    for d in range(1, min(i_max-i, j+1-0)): # SW direction
        if seating_matrix[i+d,j-d]==1:
            sum_adj_occ += 1
            break
    return sum_adj_occ


def print_seating_matrix(seating_matrix):
    for row in seating_matrix:
        for element in row:
            if element == 1:
                print('#', end='')
            elif element == 0:
                print('L', end='')
            elif element == -1:
                print('.', end='')
            else:  # shouldn't do this
                print('x', end='')
        print('')
    print('\n--------------------------------')


if __name__=='__main__':
    # in_filename = r'data\day11_in.txt'
    in_filename = r'data\test11.txt'
    in_data = np.loadtxt(in_filename, dtype=str)
    id_map = {'L': 0, r'#': 1, '.': -1}
    in_data2 = np.array([[id_map[seat] for seat in row] for row in in_data])
    print('Part 2 solution: ' + str(part2(in_data2)))