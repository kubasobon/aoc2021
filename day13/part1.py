import colorama


def flip(grid, x_axis=False, y_axis=False):
    assert x_axis or y_axis
    new = {}
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())
    for x, y in self.grid.keys():
        nx = x if not x_axis else max_x - x
        ny = y if not y_axis else max_y - y
        new[(x, y)] = grid[(x, y)]
    return new


def parse_data(data) -> (Layer, list):
    grid = {}
    folds = []
    for i, l in enumerate(data):
        if l == "":
            break
        x, y = l.split(",")
        grid[(x, y)] = True

    # ("y", 7), ("x", 5)
    folds = [l.split()[-1].split("=") for l in data[i:]]
    return Layer(grid), folds


class Layer:
    def __init__(self, grid: dict[(int, int):bool]):
        self.grid = grid

    def fold(self, axis: str, position: int) -> Layer:
        this, new = {}, {}
        for x, y in self.grid.keys():
            coords = {"x": x, "y": y}
            if coords[axis] > position:
                new[(x, y)] = self.grid[(x, y)]
            else:
                this[(x, y)] = self.grid[(x, y)]
        new = flip(new, axis == "x", axis == "y")
        self.grid = this
        return new

    def draw(self):
        max_x = max(x for x, y in self.grid.keys())
        max_y = max(y for x, y in self.grid.keys())
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) in self.grid:
                    print(colorama.Fore.YELLOW + "#", end=colorama.Style.RESET_ALL)
                else:
                    print(".", end="")
            print()


if __name__ == "__main__":
    test_data = [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5",
    ]

    data = test_data
    layer, folds = parse_data(data)
    layer.draw()
