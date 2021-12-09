import string


def make_cave_map(data):
    m = {}
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            m[(x, y)] = int(height)
    return m, x + 1, y + 1


def find_local_min(m, mx, my):
    local_min = []
    for y in range(my):
        for x in range(mx):
            v = m[(x, y)]
            if y > 0 and m[(x, y - 1)] <= v:
                continue
            if x < mx - 1 and m[(x + 1, y)] <= v:
                continue
            if y < my - 1 and m[(x, y + 1)] <= v:
                continue
            if x > 0 and m[(x - 1, y)] <= v:
                continue
            local_min.append((x, y))
    return local_min


def get_risk(m, local_min):
    return sum(m[coords] + 1 for coords in local_min)


def find_basin(m, mx, my, minimum):
    basin = []
    to_check = [minimum]
    while len(to_check) > 0:
        to_check_new = []
        for x, y in to_check:
            to_check_new.append((x, y - 1))
            to_check_new.append((x, y + 1))
            to_check_new.append((x - 1, y))
            to_check_new.append((x + 1, y))
        # sanity
        to_check_new = [
            (x, y)
            for x, y in to_check_new
            if (x, y) not in basin and x >= 0 and x < mx and y >= 0 and y < my
        ]
        # rules
        to_check_new = [coords for coords in to_check_new if m[coords] < 9]
        basin.extend(to_check)
        to_check = to_check_new
    return basin


if __name__ == "__main__":
    test_data = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f.readlines()]

    data = test_data
    m, mx, my = make_cave_map(data)
    local_min = find_local_min(m, mx, my)
    basins = [find_basin(m, mx, my, minimum) for minimum in local_min]
    for b in basins:
        print(len(b), ":   ", b)
