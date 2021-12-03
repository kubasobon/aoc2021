import string

with open("input.txt") as f:
    data = f.readlines()
data = [l.strip(string.whitespace) for l in data]

sum_position = [0] * len(data[0])
for l in data:
    for position, value in enumerate(l):
        sum_position[position] += int(value)

most_common = ""
least_common = ""
for value in sum_position:
    if value > len(data) / 2:
        most_common += "1"
        least_common += "0"
    else:
        most_common += "0"
        least_common += "1"

gamma = int(most_common, 2)
epsilon = int(least_common, 2)
print(f"Gamma x Epsilon: {gamma*epsilon}")
