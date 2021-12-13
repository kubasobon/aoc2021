class Cave:
    def __init__(self, name):
        self.name = name
        self.tunnels = []

    def is_small(self):
        return self.name.islower() and self.name not in ("start", "end")

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

class Path:
    def __init__(self, caves):
        self.caves = caves

    def __len__(self):
        return len(self.caves)

    def __repr__(self):
        return " -> ".join(str(c) for c in self.caves)


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


def walk_cave_system(cave, path_so_far=None):
    if path_so_far is None:
        path_so_far = []
    # print(f"{path_so_far} -> {cave}")
    # breakpoint()
    path_so_far.append(cave)
    if cave.is_end():
        return Path(path_so_far)
    tunnel_paths = []
    for t in cave.tunnels:
        if t.is_start():
            continue
        if t.is_small() and t in path_so_far:
            continue
        tunnel_paths.append(walk_cave_system(t, path_so_far[:]))
    return [p for p in tunnel_paths if len(p) > 0]

def flatten_the_walk(walk):
    paths = []
    for x in walk:
        if isinstance(x, list):
            paths.extend(flatten_the_walk(x))
        elif isinstance(x, Path):
            paths.append(x)
        else:
            raise TypeError("Cannot flatten this")
    return paths



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
    # print_cave_system(start)
    walk = walk_cave_system(start)
    for path in flatten_the_walk(walk):
        print(path)
