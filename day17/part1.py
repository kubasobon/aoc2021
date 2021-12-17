def contains(rect, point_x, point_y):
    xa, ya, xb, yb = rect
    return xa <= point_x <= xb and yb <= point_y <= ya


def sign(a):
    return 1 if a >= 0 else -1


def overshot(rect, point_x, point_y):
    xa, ya, xb, yb = rect
    return point_x > xb or point_y < yb


def launch_probe(vx, vy, target):
    txa, tya, txb, tyb = target

    x, y, max_y = 0, 0, 0
    while not overshot(target, x, y):
        x += vx
        y += vy
        max_y = max(max_y, y)
        # print(f"v=({vx}, {vy}), pos=({x}, {y}), max_y={max_y}")
        if vx != 0:
            vx -= sign(vx)  # drag
        vy -= 1  # gravity
        if contains(target, x, y):
            return True, max_y
    return False, max_y


if __name__ == "__main__":
    t = (20, -5, 30, -10)
    t = (185, -74, 221, -122)
    assert sign(t[0]) > 0 and sign(t[2]) > 0
    assert sign(t[1]) < 0 and sign(t[3]) < 0

    hits = {}
    for vy in range(1, 100):
        for vx in range(1, t[2]):
            hit, max_y = launch_probe(vx, vy, t)
            if hit:
                hits[(vx, vy)] = max_y

    max_y = max(hits.values())
    for v, y in hits.items():
        if y == max_y:
            print(f"velocity={v} -> altitude={max_y}")
