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


class Octopus:
    def __init__(self, energy):
        self.e = energy
        self.neighbours = []
        self.__flashed_this_step = False

    def inc(self) -> None:
        self.e += 1

    def flash(self) -> bool:
        if self.e > 9:
            self.e = 0
            for n in self.neighbours:
                n.inc()
            self.__flashed_this_step = True
            return True
        return False

    def reset(self):
        if self.__flashed_this_step:
            self.e = 0
        self.__flashed_this_step = False


def build_cave(data: list) -> dict:
    grid = {}
    for y, row in enumerate(data):
        for x, s in enumerate(row):
            grid[(x, y)] = Octopus(int(s))

    for coord, o in grid.items():
        x, y = coord
        for dx, dy in __adjacency:
            nx = x + dx
            ny = y + dy
            try:
                o.neighbours.append(grid[(nx, ny)])
            except KeyError:
                pass

    return grid


def draw_map(grid: dict) -> None:
    max_y = max(y for _, y in grid)
    max_x = max(x for x, _ in grid)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            v = grid[(x, y)].e
            if v == 0:
                print(colorama.Fore.YELLOW + str(v), end=colorama.Style.RESET_ALL)
            else:
                print(v, end="")
        print()


def step(grid: dict) -> int:
    for o in grid.values():
        o.inc()
    flashes = 0
    new_flashes = 1
    while new_flashes > 0:
        new_flashes = sum(1 if o.flash() else 0 for o in grid.values())
        flashes += new_flashes
    for o in grid.values():
        o.reset()
    return flashes


if __name__ == "__main__":
    colorama.init()
    test_data = [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526",
    ]
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    grid = build_cave(data)
    total_flashes = 0
    for i in range(100):
        flashes = step(grid)
        total_flashes += flashes
        print(f"{i+1}: {flashes}")
        # draw_map(grid)
        # breakpoint()
    print(f"TOTAL: {total_flashes}")
