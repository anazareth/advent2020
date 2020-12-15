# Problem: https://adventofcode.com/2020/day/15
# Date: December 2020
# Author: Alex Nazareth


def part1(start_nums, end_num):
    num_list = [int(s) for s in start_nums]
    last_said = {s: i for i, s in enumerate(num_list[:-1])}
    for i in range(len(num_list), end_num):
        last_num = num_list[-1]
        if last_num not in last_said:
            last_said[last_num] = i-1
            num_list.append(0)
        else:
            diff = i - 1 - last_said[last_num]
            last_said[last_num] = i-1
            num_list.append(diff)
    return num_list[-1]


def part2(start_nums, end_num):
    last_num = start_nums[-1]  # only need last number, not whole history (because of 'last_said' on next line)
    last_said = {s: i for i, s in enumerate(start_nums[:-1])}  # remember last occurrence of each unique int
    for i in range(len(start_nums), end_num):
        if last_num not in last_said:
            last_said[last_num] = i - 1
            last_num = 0
        else:
            diff = i - 1 - last_said[last_num]
            last_said[last_num] = i - 1
            last_num = diff
    return last_num


if __name__ == '__main__':
    test_input = [int(i) for i in '6,3,15,13,1,0'.split(',')]  # actual test input
    print('Part 1 answer is: ' + str(part2(test_input, 2020)))
    print('Part 2 answer is: ' + str(part2(test_input, 30000000)))

