#! /usr/bin/python3
import string

with open("input.txt") as f:
    data = f.readlines()
data = [l.strip(string.whitespace) for l in data]

def filter_data(data, use_most_common, default):
    remaining_data = data[:]
    position = 0
    while len(remaining_data) > 1 and position < len(data[0]):
        total = 0
        for line in remaining_data:
            total += int(line[position])

        filter_sign = ""
        most_common = 1 if total > len(remaining_data) / 2 else 0
        eq = total == len(remaining_data) / 2
        # print(f"mc: {most_common}\neq: {eq}")
        if eq:
            filter_sign = default
        else:
            if use_most_common:
                filter_sign = str(most_common)
            else:
                filter_sign = "1" if most_common == 0 else "0"
        # print(f"filter sign: {filter_sign}")

        remaining_data = [
            line for line in remaining_data
            if line[position] == filter_sign
        ]
        position += 1
    assert len(remaining_data) == 1
    return remaining_data[0]

oxygen = int(filter_data(data, True, "1"), 2)
co2 = int(filter_data(data, False, "0"), 2)
# print(oxygen)
# print(co2)
print(f"{oxygen * co2}")
