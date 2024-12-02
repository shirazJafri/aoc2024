#!/usr/bin/env python3

def safe(report_from_file):
    differences = diffs(report_from_file)
    all_positive = all(diff > 0 for diff in differences)
    all_negative = all(diff < 0 for diff in differences)
    diff_within_3 = all(1 <= abs(diff) <= 3 for diff in differences)

    return (all_positive or all_negative) and diff_within_3


def diffs(list_of_values):
    return [list_of_values[i] - list_of_values[i - 1] for i in range(1, len(list_of_values))]

no_of_safe_reports = 0
with open('input.txt') as reports:
    for report in reports:
        report = list(map(int, report.split()))
        no_of_safe_reports += 1 if safe(report) else 0

print(f'Total number of safe reports: {no_of_safe_reports}.')