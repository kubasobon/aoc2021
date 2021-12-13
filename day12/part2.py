import string
from collections import Counter
from functools import cache


class Cave:
    def __init__(self, name):
        self.name = name
        self.tunnels = []
        self.__hash = None

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

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        if self.__hash is None:
            self.__hash = hash(f"{self.name}: {self.tunnels}")
        return self.__hash


class Path:
    def __init__(self, caves):
        self.caves = caves
        self.__hash = None

    def __len__(self):
        return len(self.caves)

    def __repr__(self):
        return " -> ".join(str(c) for c in self.caves)

    def __eq__(self, other):
        return self.caves == other.caves

    def __hash__(self):
        if self.__hash is None:
            self.__hash = hash(tuple(self.caves))
        return self.__hash


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

    # figure out the most visited cave
    small_caves = Counter(c for c in path_so_far if c.is_small())
    if len(small_caves.most_common()) > 0:
        mc_cave, mc_count = small_caves.most_common()[0]
    else:
        mc_cave = None
        mc_count = 0
    tunnel_paths = []
    for t in cave.tunnels:
        if t.is_start():
            continue
        if t.is_small():
            if t in path_so_far:
                if mc_count == 2:
                    continue
                else:
                    tunnel_paths.append(walk_cave_system(t, path_so_far[:]))
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
    return list(set(paths))


if __name__ == "__main__":
    test_data_a = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]
    test_data_b = [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ]
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    start = build_cave_system(data)
    # print_cave_system(start)
    walk = walk_cave_system(start)
    paths = flatten_the_walk(walk)
    print(f"There are {len(paths)} paths that visit small caves at most once.")
