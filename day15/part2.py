import sys
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


def enlarge_map(grid, bounds):
    new_grid = {}
    max_x, max_y = bounds[0] + 1, bounds[1] + 1
    for y in range(max_x * 5):
        for x in range(max_y * 5):
            quad_x = int(x / max_x)
            quad_y = int(y / max_y)
            original_x = x % max_x
            original_y = y % max_y
            risk = grid[original_x, original_y] + quad_x + quad_y
            if risk > 9:
                risk = risk % 10 + 1
            new_grid[(x, y)] = risk
    return new_grid


def dijkstra(grid, start, bounds):
    max_x, max_y = bounds
    visited = {start: 0}
    pathmaker = {}
    nodes = set(x for x in grid)
    print(f"Dijkstra for {len(grid)} nodes: ", flush=True)

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
        if len(visited) % 1000 == 0:
            print(f"+ {len(visited)}", end="\r", flush=True)

    print()
    return visited, pathmaker


def make_path(pathmaker, start, end):
    path = []
    last = start
    while last != end:
        path.append(last)
        last = pathmaker[last]
    path.append(last)
    return path[::-1]


def draw_map(grid, path):
    max_y = max(y for x, y in grid)
    max_x = max(x for x, y in grid)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
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
    # data = test_data
    grid, end = parse_risk_map(data)
    grid = enlarge_map(grid, end)
    end = ((end[0] + 1) * 5 - 1, (end[1] + 1) * 5 - 1)
    visited, pathmaker = dijkstra(grid, (0, 0), end)
    path = make_path(pathmaker, end, (0, 0))
    print("Path of lowest risk:")
    # draw_map(grid, path)
    # starting point cost does not count
    risk = sum(grid[coords] for coords in path) - grid[(0, 0)]
    print(f"\nrisk={risk}")
