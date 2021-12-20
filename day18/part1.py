import math
from collections import Counter


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
        if self.level >= 4:
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
                p.right.leftmost().left += self.right
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


if __name__ == "__main__":
    data = [
        "[[[[[9,8],1],2],3],4]",
        "[7,[6,[5,[4,[3,2]]]]]",
        "[[6,[5,[4,[3,2]]]],1]",
        "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
        "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
    ]
    for d in data:
        l = eval(d)
        tree = Node(None, 0, l)
        print(tree, end=" -> ")
        print(tree.leftmost_lvl4())
        tree.leftmost_lvl4().explode()
        print(tree)
        print()

    data = [
        "[[[[0,7],4],[15,[0,13]]],[1,1]]",
        "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
    ]
    for d in data:
        l = eval(d)
        tree = Node(None, 0, l)
        print(tree, end=" -> ")
        print(tree.leftmost_splittable())
        tree.leftmost_splittable().split()
        print(tree)
        print()
