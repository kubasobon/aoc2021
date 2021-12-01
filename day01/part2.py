import string

with open('input.txt') as f:
    data = [
        int(line.strip(string.whitespace))
        for line in f.readlines()
    ]

windows = [
    data[i] + data[i+1] + data[i+2]
    for i in range(len(data)-2)
]

delta_positive = 0
for i, window in enumerate(windows):
    if i == 0:
        continue
    if windows[i-1] < window:
        delta_positive += 1

print(f'Depth increases: {delta_positive}')

