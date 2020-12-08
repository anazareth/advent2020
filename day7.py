# Problem: https://adventofcode.com/2020/day/7
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt


def part1():
    in_filename = r'data\day7_in.txt'
    # in_filename = r'data\test7.txt'
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
    print('part 1 answer: ' + str(num_bags))
    return G

    # pos=nx.spring_layout(G) # positions for all nodes
    # nx.draw_networkx_nodes(G,pos,
    #                         node_color='b',
    #                         node_size=500,
    #                     alpha=0.8)
    # nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    # plt.show()


def part2(G):
    root_node = 'shiny gold'
    bag_sum = sum_bags(G, root_node)
    print('part 2 answer: ' + str(bag_sum))


def parse_colour(bag_colour, inner_colour):
    x = re.search(r'(^[1-9]*) ([a-z]* [a-z]*).*',inner_colour)
    if x:
        colour = x.group(2)
        qty = x.group(1)
        return (bag_colour, colour, qty)
    return None

def sum_bags(G, bag_colour):
    child_bags = G.adj[bag_colour]
    if len(child_bags)==0:
        return 0
    else:
        temp = 0
        for c, w in dict(child_bags).items():
            temp += int(w['weight']) + int(w['weight'])*int(sum_bags(G, c))
            print(c,w)
        print('--')
        print(str(w['weight']) + ' + ' + str(w['weight']) + '*' + str(temp))
        return temp


if __name__=='__main__':
    G = part1()
    part2(G)