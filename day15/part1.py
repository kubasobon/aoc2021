from math import sqrt
import string
import colorama


# no diagonals
__adjacency = [
    (0, 1),
    # (1, 1),
    (1, 0),
    # (1, -1),
    (0, -1),
    # (-1, -1),
    (-1, 0),
    # (-1, 1),
]


def parse_risk_map(data):
    grid = {}
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            grid[(x, y)] = int(v)
    return grid, (x, y)


def dijkstra(grid, start, bounds):
    max_x, max_y = bounds
    visited = {start: 0}
    pathmaker = {}
    nodes = set(x for x in grid)

    while nodes:
        min_node = None
        for n in nodes:
            if n not in visited:
                continue
            if min_node is None:
                min_node = n
            elif visited[n] < visited[min_node]:
                min_node = n
        if min_node is None:
            break
        nodes.remove(min_node)
        cost = visited[min_node]

        x, y = min_node
        for dx, dy in __adjacency:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                continue
            nstart = (nx, ny)
            ncost = cost + grid[nstart]
            if nstart not in visited or ncost < visited[nstart]:
                visited[nstart] = ncost
                # if nstart not in pathmaker:
                #     pathmaker[nstart] = []
                # pathmaker[nstart].append(min_node)
                pathmaker[nstart] = min_node

    return visited, pathmaker


def make_path(pathmaker, start, end):
    path = []
    last = start
    while last != end:
        path.append(last)
        last = pathmaker[last]
    path.append(last)
    return path[::-1]


def draw_map(grid, path, bounds):
    for y in range(bounds[1] + 1):
        for x in range(bounds[0] + 1):
            if (x, y) in path:
                print(
                    colorama.Fore.YELLOW + str(grid[(x, y)]),
                    end=colorama.Style.RESET_ALL,
                )
            else:
                print(grid[(x, y)], end="")
        print()


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
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    grid, end = parse_risk_map(data)
    visited, pathmaker = dijkstra(grid, (0, 0), end)
    path = make_path(pathmaker, end, (0, 0))
    print("Path of lowest risk:")
    draw_map(grid, path, end)
    # starting point cost does not count
    risk = sum(grid[coords] for coords in path) - grid[(0, 0)]
    print(f"\nrisk={risk}")
