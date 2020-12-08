# Problem: https://adventofcode.com/2020/day/7
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt


# def part1_v1():
#     in_filename = r'data\day7_in.txt'
#     in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
 
#     bag_idx = {}
#     bag_idx['no other']=0
#     for spec in in_data:
#         bag_colour, inner_spec = spec.split(' bags contain ')
#         contents_dict = {}
#         for i in [x.replace('bags','').replace('bag','').strip('.') for x in inner_spec.split(', ')]:
#             if i.strip()!='no other':
#                 qty = i.split(' ')[0]
#                 inner_colour = i.replace(str(qty)+' ','').strip(' ')
#                 contents_dict[inner_colour] = qty
#         bag_idx[bag_colour] = contents_dict
#     target = 'shiny gold'
#     num_found = 0
#     for c in bag_idx:
#         if type(bag_idx[c]) is int:
#             if c == target:
#                 num_found +=1
#         else:
#             temp = find_colour(target, bag_idx[c], bag_idx)
#             if temp is not None:
#                 num_found += temp
#     print(num_found)


def part1():
    in_filename = r'data\day7_in.txt'
    in_data = np.loadtxt(in_filename, dtype=str, delimiter='\n')
    
    G = nx.DiGraph()
    colour_edges = []
    for row in in_data:
        bag_colour, inner_spec = row.split(' bags contain ')
        inner_colours = [parse_colour(bag_colour,c) for c in inner_spec.split(', ')]
        colour_edges += [i for i in inner_colours if i]
    G.add_weighted_edges_from(colour_edges)
    
    num_bags=0
    target = 'shiny gold'
    for b in G.nodes():
        if b!=target and nx.has_path(G,b,target):
            num_bags+=1
    print(num_bags)

    # pos=nx.spring_layout(G) # positions for all nodes
    # nx.draw_networkx_nodes(G,pos,
    #                         node_color='b',
    #                         node_size=500,
    #                     alpha=0.8)
    # nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    # plt.show()


def parse_colour(bag_colour, inner_colour):
    x = re.search(r'(^[1-9]*) ([a-z]* [a-z]*).*',inner_colour)
    if x:
        colour = x.group(2)
        qty = x.group(1)
        return (bag_colour, colour, qty)
    return None




# def find_colour(colour, spec_dict, bag_list):
#     if colour in spec_dict:
#         return 1
#     else:
#         for c in spec_dict:
#             return find_colour(colour, bag_list[c], bag_list)

def part2():
    print(-2)


if __name__=='__main__':
    part1()
    part2()