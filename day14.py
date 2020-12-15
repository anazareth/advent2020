# Problem: https://adventofcode.com/2020/day/14
# Date: December 2020
# Author: Alex Nazareth


import numpy as np


def part1(rows):
    mem = dict()
    mask = dict()
    for r in rows:
        lhs, rhs = r.split(' = ')
        if lhs == 'mask':
            mask = dict()
            for i, b in enumerate(rhs):
                if b != 'X':
                    mask[i] = b
        else:
            addr = int(lhs[4:-1])
            val_bin = '{:036b}'.format(int(rhs))
            updated_val_bin = val_bin
            for i, b in mask.items():
                updated_val_bin = updated_val_bin[:i] + b + updated_val_bin[i+1:]
            updated_val_int = int(updated_val_bin, 2)
            mem[addr] = updated_val_int
    return sum(mem.values())


def part2(rows):
    mem = dict()
    ones_mask = []
    floatings_mask = []
    for r in rows:
        lhs, rhs = r.split(' = ')
        if lhs == 'mask':
            ones_mask = []
            floatings_mask = []
            for i, b in enumerate(rhs):
                if b == '1':
                    ones_mask.append(i)
                elif b == 'X':
                    floatings_mask.append(i)
        else:
            addr, val = int(lhs[4:-1]), int(rhs)
            addr_bin = '{:036b}'.format(int(addr))
            # create masked memory address, and then handle "floating" bits
            updated_addr_bin = addr_bin
            for i in ones_mask:
                updated_addr_bin = updated_addr_bin[:i] + '1' + updated_addr_bin[i+1:]
            for i in floatings_mask:
                updated_addr_bin = updated_addr_bin[:i] + 'X' + updated_addr_bin[i+1:]
            mem_locations = set()
            mem_locations = get_mem_locs(updated_addr_bin, floatings_mask, mem_locations)
            for m in mem_locations:
                mem[int(m, 2)] = val
    return sum(mem.values())


def get_mem_locs(binary_addr, floats, mem_locs):
    # recursive function to get all permutations of memory locations due to "floating" positions
    float_loc = floats[0]
    updated_binary_addr = [0, 0]
    for i in [0, 1]:  # two "child" cases - subbing 0 or 1
        updated_binary_addr[i] = binary_addr[:float_loc] + str(i) + binary_addr[float_loc+1:]
        if 'X' not in updated_binary_addr[i]:  # base case
            mem_locs = mem_locs.union([updated_binary_addr[i]])
        else:
            mem_locs = mem_locs.union(get_mem_locs(updated_binary_addr[i], floats[1:], mem_locs))
    return mem_locs


if __name__ == '__main__':
    in_filename = r'data\day14_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    print('Answer for part 1: ' + str(part1(in_data)))
    print('Answer for part 2: ' + str(part2(in_data)))
