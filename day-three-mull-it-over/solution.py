#!/usr/bin/env python3
import re


def extract_mul_from_memory_location(location):
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', location.strip())


def mul_result_for_location(location):
    sum_of_multiplications = 0
    matches = extract_mul_from_memory_location(location)
    for match in matches:
        match = re.sub(r'[()]', '', match.replace('mul', ''))
        first, second = list(map(int, match.split(',')))
        sum_of_multiplications += first * second

    return sum_of_multiplications


with open('input.txt') as corrupted_memory_locations:
    sum_of_all_locations = sum(
        mul_result_for_location(memory_location) for memory_location in corrupted_memory_locations)

print(f'The sum of all `mul` in corrupted memory locations is {sum_of_all_locations}')
