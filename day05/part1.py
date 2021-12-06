import string


def print_map(b):
    max_x = max(coords[0] for coords in b.d)
    max_y = max(coords[1] for coords in b.d)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            s = str(b.get(x, y))
            print(s, end=" ")
        print("")


class VentMap:
    def __init__(self):
        self.d = {}

    def get(self, x, y):
        if (x, y) not in self.d:
            return 0
        return self.d[(x, y)]

    def inc(self, x, y):
        if (x, y) not in self.d:
            self.d[(x, y)] = 0
        self.d[(x, y)] += 1

    def map_line(self, x1, y1, x2, y2):
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1
        dist_x = x2 - x1
        dist_y = y2 - y1
        if dist_x == 0:
            for y in range(y1, y2 + 1):
                self.inc(x1, y)
        elif dist_y == 0:
            for x in range(x1, x2 + 1):
                self.inc(x, y1)
        # print(x1, x2, y1, y2)
        # print_map(self)
        # breakpoint()

    def overlaps(self):
        return sum(1 for v in self.d.values() if v >= 2)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()

    vent_map = VentMap()
    for line in data:
        line = line.strip(string.whitespace)
        a, b = line.split(" -> ")
        x1, y1 = (int(n) for n in a.split(","))
        x2, y2 = (int(n) for n in b.split(","))
        vent_map.map_line(x1, y1, x2, y2)
        # print(line)
        # print_map(vent_map)
        # breakpoint()

    print(f"{vent_map.overlaps()}")
