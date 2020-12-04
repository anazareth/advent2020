# Problem: https://adventofcode.com/2020/day/1
# Date: December 2020
# Author: Alex Nazareth

import numpy as np

def part1():
    in_filename = 'day3_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n', comments=None)

    in_width, ymax = len(in_data[0]), len(in_data)
    xpos, ypos = 0, 0
    num_trees = 0

    while ypos<ymax-1:
        xpos = (xpos + 3)%in_width
        ypos += 1
        if in_data[ypos][xpos]=='#':
            num_trees += 1
    return num_trees

def part2(dx, dy):
    in_filename = 'day3_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n', comments=None)

    in_width, ymax = len(in_data[0]), len(in_data)
    xpos, ypos = 0, 0
    num_trees = 0

    while ypos<ymax-1:
        xpos = (xpos + dx)%in_width
        ypos += dy
        if in_data[ypos][xpos]=='#':
            num_trees += 1
    return num_trees


if __name__=='__main__':
    print(part2(1,1)*part2(3,1)*part2(5,1)*part2(7,1)*part2(1,2))
