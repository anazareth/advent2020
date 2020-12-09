# Problem: https://adventofcode.com/2020/day/8
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re
import networkx as nx


def part1(in_data):
    instr_counter = np.zeros(len(in_data), dtype=int)
    acc = 0
    cmd_pos = 0
    while True:
        if cmd_pos>len(in_data)-1 or instr_counter[cmd_pos]>0:
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


def part2(in_data):
    n = len(in_data)
    G = nx.DiGraph()
    for i in range(n):
        cmd, val = in_data[i][0:3], int(in_data[i][3:])
        G.add_node(i, cmd = cmd, val = val)
        if cmd in ['acc','nop']:
            G.add_edge(i, i+1)
        else:
            G.add_edge(i, i+val)
    i = 0
    end_node = n-1
    while True:
        cmd, val = G.nodes()[i]['cmd'], int(G.nodes()[i]['val'])
        next_node = list(G.adj[i])[0]  # since there is always only 1 out node
        if cmd == 'jmp':
            G.add_edge(i, i+1)
            if nx.has_path(G, i, end_node):
                in_data[i] = in_data[i].replace('jmp','nop')
                print('change from jmp to nop at row ' + str(i))
                return part1(in_data)
            else:
                G.remove_edge(i, i+1)
        elif cmd == 'nop':
            G.add_edge(i, i+val)
            if nx.has_path(G, i, end_node):
                in_data[i] = in_data[i].replace('nop','jmp')
                print('change from nop to jmp at row ' + str(i))
                return part1(in_data)
            else:
                G.remove_edge(i, i+val)
        else:
            pass
        i = next_node


if __name__=='__main__':
    in_filename = r'data\day8_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    print('Part 1 solution: ' + str(part1(in_data)))
    print('Part 2 solution: ' + str(part2(in_data)))
