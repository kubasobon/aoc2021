import colorama


class Layer:
    def __init__(self, grid):
        self.grid = grid

    def fold(self, axis: str, position: int):
        this, new = {}, {}
        for x, y in self.grid:
            coords = {"x": x, "y": y}
            if coords[axis] > position:
                new[(x, y)] = self.grid[(x, y)]
            else:
                this[(x, y)] = self.grid[(x, y)]
        new = flip(new, axis == "x", axis == "y")
        self.grid = this
        return new

    def draw(self):
        max_x = max(x for x, y in self.grid)
        max_y = max(y for x, y in self.grid)
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) in self.grid:
                    print(colorama.Fore.YELLOW + "#", end=colorama.Style.RESET_ALL)
                else:
                    print(".", end="")
            print()

    def merge(self, new_grid):
        for x, y in new_grid:
            self.grid[(x, y)] = True


def parse_data(data: list):
    grid = {}
    folds = []
    for i, l in enumerate(data):
        if l == "":
            break
        x, y = l.split(",")
        grid[(int(x), int(y))] = True

    # ("y", 7), ("x", 5)
    folds = [l.split()[-1].split("=") for l in data[i + 1 :]]
    folds = [(axis, int(pos)) for axis, pos in folds]
    return Layer(grid), folds


def flip(grid: dict, x_axis: bool = False, y_axis: bool = False) -> dict:
    assert x_axis or y_axis
    new = {}
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    for x, y in grid:
        nx = x if not x_axis else max_x - x
        ny = y if not y_axis else max_y - y
        new[(nx, ny)] = grid[(x, y)]
    return new


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
    print("\n")
    for fold in folds:
        print(f"Folded along {fold[0]}={fold[1]}")
        new_grid = layer.fold(*fold)
        layer.merge(new_grid)
        layer.draw()
        print("\n")
    pts = sum(1 for _ in layer.grid)
    print(f"Visible points: {pts}")
