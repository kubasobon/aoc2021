import colorama
import string
from PIL import Image, ImageDraw


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
        new = flip(new, position, axis == "x", axis == "y")
        this.update(new)
        self.grid = this

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
        self.grid.update(new_grid)


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


def flip(grid: dict, position: int, x_axis: bool = False, y_axis: bool = False) -> dict:
    assert x_axis or y_axis
    new = {}
    for x, y in grid:
        nx = x if not x_axis else 2 * position - x
        ny = y if not y_axis else 2 * position - y
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

    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    # data = test_data
    layer, folds = parse_data(data)
    for i, fold in enumerate(folds):
        print(f"Folded along {fold[0]}={fold[1]}")
        layer.fold(*fold)
        if i == 0:  # part1
            pts = sum(1 for _ in layer.grid)
            print(f"Points visible after 1st fold: {pts}")
    layer.draw()
