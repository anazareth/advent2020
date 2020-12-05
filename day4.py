# Problem: https://adventofcode.com/2020/day/4
# Date: December 2020
# Author: Alex Nazareth

import numpy as np
import re


def part1():
    in_filename = r'data\day4_in.txt'
    passports = parse_passports(in_filename)
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']  # cid excl.
    num_req_fields = [7,8]

    count_valid = 0
    for p in passports:
        if len(p) in num_req_fields and \
            set(p.keys()).union({'cid'})==set(required_fields).union({'cid'}):
            count_valid += 1
    print(count_valid)


def part2():
    in_filename = r'data\day4_in.txt'
    passports = parse_passports(in_filename)
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']  # cid excl.
    num_req_fields = [7,8]

    count_valid = 0
    for p in passports:
        if len(p) in num_req_fields and \
            set(p.keys()).union({'cid'})==set(required_fields).union({'cid'}):
            if int(p['byr'])>=1920 and int(p['byr'])<=2002 and \
                int(p['iyr'])>=2010 and int(p['iyr'])<=2020 and \
                int(p['eyr'])>=2020 and int(p['eyr'])<=2030 and \
                check_height(p['hgt']) and \
                bool(re.match(r'^\#[0-9a-zA-Z]{6}$', p['hcl'])) and \
                p['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and \
                bool(re.match(r'^[0-9]{9}$', p['pid'])) :
                count_valid += 1
    print(count_valid)
    

def parse_passports(passports_filename):
    with open(passports_filename) as f:
        passports_list = []
        pport_str = ''
        for line in f.readlines():
            pport_str = pport_str + ' ' + line.strip('\n')
            if line=='\n':
                passports_list.append(pport_str_to_dict(pport_str))
                pport_str=''
        passports_list.append(pport_str_to_dict(pport_str))
    return passports_list

def pport_str_to_dict(pport_str):
    pport = {}
    for field in [f for f in pport_str.split(sep=' ') if f != '']:
        key, val = field.split(':')
        pport[key] = val
    return pport

def check_height(height_str):
    if len(height_str)>2:
        unit = height_str[-2:]
        val =  int(height_str[:-2])
        if unit == 'cm':
            return 150<=val and val<=193
        elif unit =='in':
            return 59<=val and val<=76
    return False

if __name__=='__main__':
    part2()