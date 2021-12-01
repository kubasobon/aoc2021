import string

with open('input.txt') as f:
    data = [
        int(line.strip(string.whitespace))
        for line in f.readlines()
    ]


delta_positive = 0
for i, depth in enumerate(data):
    if i == 0:
        continue
    if data[i-1] < depth:
        delta_positive += 1

print(f'Depth increases: {delta_positive}')
