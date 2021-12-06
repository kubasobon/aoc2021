import string
from collections import Counter


def process_a_day(lanternfish):
    cpy = Counter()
    cpy[8] = 0
    for age, count in lanternfish.items():
        if count == 0:
            continue
        if age == 0:
            cpy[6] += count
            cpy[8] += count
        else:
            cpy[age - 1] += count
    return cpy


if __name__ == "__main__":
    test_input = "3,4,3,1,2"
    with open("input.txt") as f:
        data = f.readline().strip(string.whitespace)
    days = 256
    lanternfish = Counter(int(x) for x in data.split(","))
    for day in range(days):
        lanternfish = process_a_day(lanternfish)
    print(f"{day+1}: {sum(lanternfish.values())}")
