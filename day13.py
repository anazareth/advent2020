# Problem: https://adventofcode.com/2020/day/13
# Date: December 2020
# Author: Alex Nazareth


import numpy as np


def part1(bus_data, edt):
    # edt = earliest depart time
    bus_list = [int(b) for b in bus_data if b != 'x']
    print(bus_list)
    closest_bus = -1
    waiting_time = max(bus_list)
    for bus_id in bus_list:
        soonest_bus_departure = np.ceil(edt/bus_id)*bus_id
        if (soonest_bus_departure - edt) < waiting_time:
            closest_bus = bus_id
            waiting_time = soonest_bus_departure - edt
    return waiting_time * closest_bus


def part2(bus_data):
    bus_dict = dict()
    for b_idx in range(len(bus_data)):
        if bus_data[b_idx]=='x':
            continue
        else:
            bus_dict[int(bus_data[b_idx])] = -b_idx
    return chinese_remainder(bus_dict.keys(), bus_dict.values())


# the next two functions are an implementation of the chinese remainder theorem
# source: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__=='__main__':
    in_filename = r'data\day13_in.txt'
    # in_filename = r'data\test13.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    edt, bus_data = int(in_data[0]), in_data[1].split(',')
    print('Part 1 solution: ' + str(part1(bus_data, edt)))
    print('Part 2 solution: ' + str(part2(bus_data)))