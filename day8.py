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
        print(cmd_pos)
        # print(in_data[cmd_pos])
        if cmd == 'acc':
            acc += int(in_data[cmd_pos][3:])
            cmd_pos += 1
        elif cmd == 'jmp':
            cmd_pos += int(in_data[cmd_pos][3:])
        else:
            cmd_pos += 1
        # print(acc)
        # print('----')


# def part2_old(in_data):
#     cmd_pos = len(in_data)-1  # start at bottom
#     # we need our "second to last" steps  to land after the last negative jump
#     while True:
#         cmd = in_data[cmd_pos][0:3]
#         if cmd == 'jmp':
#             if int(in_data[cmd_pos][3:])<0:
#                 last_neg_jmp = cmd_pos
#                 break
#         cmd_pos += -1
    
#     last_row = len(in_data)-1
#     for row in range(1, last_row+1):
#         cmd, val= in_data[row][0:3], int(in_data[row][3:])
#         # print(cmd+':'+str(val))
#         if cmd == 'jmp':
#             temp_in_data = in_data.copy()
#             temp_in_data[row] = temp_in_data[row].replace('jmp','nop')
#             if reachable(temp_in_data, 0, row, set()) and \
#                 reachable(temp_in_data, row, last_row, set()):
#                 print('changed jmp to nop in row ' + str(row))
#                 return part1(temp_in_data)
#         elif cmd == 'nop' and val != 0:
#             temp_in_data = in_data.copy()
#             temp_in_data[row] = temp_in_data[row].replace('nop','jmp')
#             if reachable(temp_in_data, 0, row, set()) and \
#                 reachable(temp_in_data, row, last_row, set()):
#                 print('changed nop to jmp in row ' + str(row))
#                 return part1(temp_in_data)
#         else:
#             pass
#     return('didnt work')


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
                print('TODO: change from jmp to nop at row ' + str(i))
                return part1(in_data)
            else:
                G.remove_edge(i, i+1)
        elif cmd == 'nop':
            G.add_edge(i, i+val)
            if nx.has_path(G, i, end_node):
                in_data[i] = in_data[i].replace('nop','jmp')
                print('TODO: change from nop to jmp at row ' + str(i))
                return part1(in_data)
            else:
                G.remove_edge(i, i+val)
        else:
            pass
        i = next_node


# def reachable_range(in_data, row_a, last_neg_jmp, visited):
#     # recursively check if starting from row_a gets us to the "home stretch"
#     if row_a in visited:
#         return False
#     else:
#         visited.add(row_a)
#     instr_a = in_data[row_a]
#     cmd = instr_a[0:3]
#     if cmd in ['nop','acc'] and row_a + 1 > last_neg_jmp:
#         return True
#     elif cmd == 'jmp':
#         jmp_val = int(instr_a[3:])
#         if row_a + jmp_val > last_neg_jmp:
#             return True
#         else:
#             return reachable_range(in_data, row_a+jmp_val, last_neg_jmp, visited)
#     else:
#         return reachable_range(in_data, row_a+1, last_neg_jmp, visited)


# def reachable(in_data, row_a, row_b, visited):
#     # recursively check if starting from row_a gets us to the "home stretch"
#     if row_a in visited:
#         return False
#     else:
#         visited.add(row_a)
#     instr_a = in_data[row_a]
#     cmd = instr_a[0:3]
#     if cmd in ['nop','acc'] and row_a + 1 == row_b:
#         return True
#     elif cmd == 'jmp':
#         jmp_val = int(instr_a[3:])
#         if row_a + jmp_val == row_b:
#             return True
#         else:
#             return reachable_range(in_data, row_a+jmp_val, row_b, visited)
#     else:
#         return reachable_range(in_data, row_a+1, row_b, visited)


if __name__=='__main__':
    in_filename = r'data\day8_in.txt'
    # in_filename = r'data\test8b.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    # print(part1(in_data))
    print(part2(in_data))