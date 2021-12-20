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
        success = False
        while p is not None:
            if p.right is not self and isinstance(p.right, int):
                    p.right += self.right
                    success = True
                    break
            if p.parent is None:
                break
            p = p.parent
        if not success:
            p.right.leftmost().left += self.right

        p = self.parent
        success = False
        while p is not None:
            if p.left is not self and isinstance(p.left, int):
                    p.left += self.left
                    success = True
                    break
            if p.parent is None:
                break
            p = p.parent
        if not success:
            p.left.rightmost().right += self.left
        if self.parent.left is self:
            self.parent.left = 0
        else:
            self.parent.right = 0


if __name__ == "__main__":
    data = [
        # "[[[[[9,8],1],2],3],4]",
        # "[7,[6,[5,[4,[3,2]]]]]",
        # "[[6,[5,[4,[3,2]]]],1]",
        "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
        # "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
    ]
    for d in data:
        l = eval(d)
        tree = Node(None, 0, l)
        print(tree, end=" -> ")
        print(tree.leftmost_lvl4())
        tree.leftmost_lvl4().explode()
        print(tree)
        print()
