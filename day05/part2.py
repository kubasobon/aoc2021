import string


def print_map(b):
    max_x = max(coords[0] for coords in b.d)
    max_y = max(coords[1] for coords in b.d)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            s = str(b.get(x, y))
            if s == "0":
                s = "."
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
        step_x = step_y = 1
        if x2 < x1:
            step_x = -1
        elif x2 == x1:
            step_x = 0
        if y2 < y1:
            step_y = -1
        elif y2 == y1:
            step_y = 0
        dist = max(abs(x2 - x1), abs(y2 - y1))
        for i in range(dist + 1):
            self.inc(
                x1 + (step_x * i),
                y1 + (step_y * i),
            )

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
