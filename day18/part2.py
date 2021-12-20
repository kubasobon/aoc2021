import string
import math


class Node:
    def __init__(self, parent, lvl, repr_):
        self.parent = parent
        self.level = lvl
        l, r = repr_
        self.left = l if isinstance(l, int) else Node(self, lvl + 1, l)
        self.right = r if isinstance(r, int) else Node(self, lvl + 1, r)

    def __repr__(self):
        return f"[{str(self.left)}, {str(self.right)}]"

    def leftmost_lvl4(self):
        if self.level >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            return self
        if isinstance(self.left, Node):
            l4 = self.left.leftmost_lvl4()
            if l4 is not None:
                return l4
        if isinstance(self.right, Node):
            l4 = self.right.leftmost_lvl4()
            if l4 is not None:
                return l4
        return None

    def leftmost_splittable(self):
        if isinstance(self.left, int):
            if self.left >= 10:
                return self
        else:
            l = self.left.leftmost_splittable()
            if l is not None:
                return l
        if isinstance(self.right, int):
            if self.right >= 10:
                return self
        else:
            r = self.right.leftmost_splittable()
            if r is not None:
                return r
        return None

    def leftmost(self):
        if isinstance(self.left, int):
            return self
        return self.left.leftmost()

    def rightmost(self):
        if isinstance(self.right, int):
            return self
        return self.right.rightmost()

    def explode(self):
        p = self.parent
        visited = [self, p]
        while p is not None:
            if p.right in visited:
                p = p.parent
                visited.append(p)
                continue
            # print(p.right, isinstance(p.right, int), isinstance(p.right, Node))
            # breakpoint()
            if isinstance(p.right, int):
                p.right += self.right
                break
            elif isinstance(p.right, Node):
                try:
                    p.right.leftmost().left += self.right
                except:
                    breakpoint()
                break
            p = p.parent
            visited.append(p)

        p = self.parent
        visited = [self, p]
        while p is not None:
            if p.left in visited:
                p = p.parent
                visited.append(p)
                continue
            if isinstance(p.left, int):
                p.left += self.left
                break
            elif isinstance(p.left, Node):
                p.left.rightmost().right += self.left
                break
            p = p.parent
            visited.append(p)

        if self.parent.left is self:
            self.parent.left = 0
        else:
            self.parent.right = 0

    def split(self):
        if isinstance(self.left, int) and self.left >= 10:
            l = math.floor(float(self.left) / 2)
            r = math.ceil(float(self.left) / 2)
            self.left = Node(self, self.level + 1, [l, r])
        elif isinstance(self.right, int) and self.right >= 10:
            l = math.floor(float(self.right) / 2)
            r = math.ceil(float(self.right) / 2)
            self.right = Node(self, self.level + 1, [l, r])

    def magnitude(self):
        l = self.left if isinstance(self.left, int) else self.left.magnitude()
        r = self.right if isinstance(self.right, int) else self.right.magnitude()
        return 3 * l + 2 * r


def process_tree(tree):
    while True:
        lvl4 = tree.leftmost_lvl4()
        if lvl4 is not None:
            lvl4.explode()
            continue
        splittable = tree.leftmost_splittable()
        if splittable is not None:
            splittable.split()
            continue
        break


def add(t1, t2):
    a = f"[{t1.__repr__()}, {t2.__repr__()}]"
    return Node(None, 0, eval(a))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]

    mags = []
    for a in range(len(data)):
        for b in range(len(data)):
            if a == b:
                continue
            tree_a = Node(None, 0, eval(data[a]))
            tree_b = Node(None, 0, eval(data[b]))
            t = add(tree_a, tree_b)
            process_tree(t)
            mags.append(t.magnitude())
    print(max(mags))
