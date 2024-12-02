#!/usr/bin/env python3

def safe(report_from_file):
    differences = diffs(report_from_file)
    all_positive = all(diff > 0 for diff in differences)
    all_negative = all(diff < 0 for diff in differences)
    diff_within_3 = all(1 <= abs(diff) <= 3 for diff in differences)
    if (all_positive and diff_within_3) or (all_negative and diff_within_3):
        return True
    else:
        return False


def diffs(list_of_values):
    diffs_to_return = []
    for i in range(1, len(list_of_values)):
        diffs_to_return.append(list_of_values[i] - list_of_values[i - 1])
    return diffs_to_return

no_of_safe_reports = 0
with open('input.txt') as reports:
    for report in reports:
        report = list(map(int, report.split()))
        if safe(report):
            no_of_safe_reports += 1

print(f'Total number of safe reports: {no_of_safe_reports}.')