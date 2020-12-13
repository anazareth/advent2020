# Problem: https://adventofcode.com/2020/day/12
# Date: December 2020
# Author: Alex Nazareth


import numpy as np


def part1(in_data):
    f_dir = 0  # forward direction, with 0 degrees = East, 90 deg = North, etc
    x, y = 0, 0  # cartesian coordinates, starting at origin
    directional_commands = {'N','E','S','W'}
    for i in in_data:
        cmd, val = i[0], int(i[1:])
        if cmd in directional_commands:
            if cmd == 'N':
                y += val
            elif cmd == 'E':
                x += val
            elif cmd == 'S':
                y += -val
            elif cmd == 'W':
                x += -val
        elif cmd == 'L':
            f_dir = (f_dir + val) % 360
        elif cmd == 'R':
            f_dir = (f_dir - val) % 360
        elif cmd == 'F':
            if f_dir == 0:
                x += val
            elif f_dir == 90:
                y += val
            elif f_dir == 180:
                x += -val
            elif f_dir == 270:
                y += -val
    return abs(x + y)


def part2(in_data):
    f_dir = 0  # forward direction, with 0 degrees = East, 90 deg = North, etc
    x, y = 0, 0  # coordinates of ship
    wx, wy = 10, 1  #coordinates of waypoint
    directional_commands = {'N','E','S','W'}
    for i in in_data:
        cmd, val = i[0], int(i[1:])
        if cmd in directional_commands:
            if cmd == 'N':
                wy += val
            elif cmd == 'E':
                wx += val
            elif cmd == 'S':
                wy += -val
            elif cmd == 'W':
                wx += -val
        elif cmd == 'L':
            if val == 90:
                temp = wx
                wx = -wy
                wy = temp
            elif val == 180:
                wx = -wx
                wy = -wy
            elif val == 270:
                temp = wy
                wy = -wx
                wx = temp
            else:
                print('bad val: ' + i)
        elif cmd == 'R':
            if val == 270:
                temp = wx
                wx = -wy
                wy = temp
            elif val == 180:
                wx = -wx
                wy = -wy
            elif val == 90:
                temp = wy
                wy = -wx
                wx = temp
            else:
                print('bad val: ' + i)
        elif cmd == 'F':
            x += val*wx
            y += val*wy
    return abs(x + y)


if __name__=='__main__':
    in_filename = r'data\day12_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    print('The solution for part 1 is ' + str(part1(in_data)))
    print('The solution for part 2 is ' + str(part2(in_data)))