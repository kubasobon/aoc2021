class Cave:
    def __init__(self, name):
        self.name = name
        self.tunnels = []

    def is_small(self):
        return self.name.islower()

    def is_start(self):
        return self.name == "start"

    def is_end(self):
        return self.name == "end"

    def add_tunnel(self, to):
        if to not in self.tunnels:
            self.tunnels.append(to)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def build_cave_system(data):
    start = None
    caves = {}
    for line in data:
        a, b = line.split("-")
        cave_a = caves[a] if a in caves else Cave(a)
        cave_b = caves[b] if b in caves else Cave(b)
        if cave_a.is_start():
            start = cave_a
        elif cave_b.is_start():
            start = cave_b
        cave_a.add_tunnel(cave_b)
        cave_b.add_tunnel(cave_a)
        caves[a] = cave_a
        caves[b] = cave_b
    return start


def print_cave_system(start):
    visited = []
    to_visit = [start]
    while len(to_visit) > 0:
        new_to_visit = []
        visited.extend(to_visit)
        for c in to_visit:
            print(f"{c.name} ({len(c.tunnels)}): {c.tunnels}")
            new_to_visit.extend(c.tunnels)
        to_visit = list(set(c for c in new_to_visit if c not in visited))


if __name__ == "__main__":
    test_data = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]
    data = test_data
    start = build_cave_system(data)
    print_cave_system(start)
