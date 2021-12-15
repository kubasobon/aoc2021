from math import sqrt
import string
import colorama


__adjacency = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


class Path(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def parse_risk_map(data):
    grid = {}
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            grid[(x, y)] = int(v)
    return grid, (x, y)


def simple_pathfinder(grid, end, pos, path_so_far=None):
    if path_so_far is None:
        path_so_far = Path()
    x, y = pos

    sep = "".join(" " for _ in path_so_far)
    psf = " ".join(str(t) for t in path_so_far)
    # print(f"{sep}{psf} -> ({x}, {y})")
    # breakpoint()


    path_so_far.append(pos)
    max_x, max_y = end
    if pos == end:
        return path_so_far
    paths = []
    for dx, dy in __adjacency:
        new_x, new_y = x + dx, y + dy
        new_pos = (new_x, new_y)
        # no crossing grid boundaries
        if new_x < 0 or new_x > max_x:
            continue
        if new_y < 0 or new_y > max_y:
            continue
        # no turning back
        if new_pos in path_so_far:
            continue
        if new_x == 0 and new_y == 0:
            continue
        # heuristics
        if distance(pos, end) < distance(new_pos, end):
            continue
        # print(f"{sep}checking ({new_x}, {new_y})")
        finds = simple_pathfinder(grid, end, (new_x, new_y), path_so_far[:])
        if isinstance(finds, Path):
            paths.append(finds)
        else:
            paths.extend(finds)
    # breakpoint()
    return [p for p in paths if len(p) > 0]

def distance(a, b):
    xa, ya = a
    xb, yb = b
    return sqrt(pow(xb-xa, 2) + pow(yb-ya, 2))

if __name__ == "__main__":
    test_data = [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581",
    ]
    data = test_data
    grid, end = parse_risk_map(data)
    paths = simple_pathfinder(grid, end, (0, 0))
    breakpoint()
    paths = flatten_paths(paths)
