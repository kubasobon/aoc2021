import string


def process_a_day(lanternfish):
    newborns = 0
    cpy = lanternfish[:]
    for i, v in enumerate(lanternfish):
        if v == 0:
            cpy[i] = 6
            newborns += 1
        else:
            cpy[i] = v - 1
    cpy.extend([8] * newborns)
    return cpy


if __name__ == "__main__":
    test_input = "3,4,3,1,2"
    with open("input.txt") as f:
        data = f.readline().strip(string.whitespace)
    days = 80
    lanternfish = [int(x) for x in data.split(",")]
    for day in range(days):
        lanternfish = process_a_day(lanternfish)
    print(f"{day+1}: {len(lanternfish)}")
