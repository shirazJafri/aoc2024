#!/usr/bin/env python3

import bisect

list_left, list_right = [], []
with open('input.txt') as input_file:
    for line in input_file:
        left, right = map(int, line.split())
        bisect.insort(list_left, left)
        bisect.insort(list_right, right)

summation_difference = sum(abs(val_left - val_right) for val_left, val_right in zip(list_left, list_right))
print(summation_difference)
