import sys
import string
from collections import Counter

BOARD_SIDE = 5
DIAGONALS = [
    [(i, i) for i in range(BOARD_SIDE)],
    [(BOARD_SIDE - i - 1, i) for i in range(BOARD_SIDE)],
]
DIAGONALS_ENABLED = False


def print_board(b):
    for y in range(BOARD_SIDE):
        for x in range(BOARD_SIDE):
            s = str(b.get(x, y))
            if len(s) == 1:
                s = " " + s
            print(s, end=" ")
        print("")


class BingoBoard:
    def __init__(self):
        self.d = {}

    @classmethod
    def from_lines(cls, lines):
        b = cls()
        for y, l in enumerate(lines):
            l = l.strip(string.whitespace).split()
            for x, num in enumerate(l):
                b.d[(x, y)] = int(num)
        return b

    def __contains__(self, num):
        return num in self.d.values()

    def get(self, x, y):
        return self.d[(x, y)]

    def call_out(self, num):
        if num not in self:
            return
        for k, v in self.d.items():
            if v == num:
                self.d[k] = "x"
                return

    def has_bingo(self):
        rows = Counter()
        cols = Counter()
        diag_a = {coords: False for coords in DIAGONALS[0]}
        diag_b = {coords: False for coords in DIAGONALS[1]}
        for k, v in self.d.items():
            if v != "x":
                continue
            row, col = k
            rows[row] += 1
            cols[col] += 1
            if k in diag_a:
                diag_a[k] = True
            if k in diag_b:
                diag_b[k] = True
        if DIAGONALS_ENABLED:
            if all(diag_a.values()) or all(diag_b.values()):
                return True
        try:
            _, total = rows.most_common(1)[0]
            if total == BOARD_SIDE:
                return True
        except IndexError:
            pass
        try:
            _, total = cols.most_common(1)[0]
            if total == BOARD_SIDE:
                return True
        except IndexError:
            pass
        return False

    def score(self, num):
        total = sum(v for v in self.d.values() if v != "x")
        return total * num


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    numbers = [int(x) for x in lines[0].strip(string.whitespace).split(",")]

    lines = lines[2:]
    boards = []
    rows = []
    for l in lines:
        l = l.strip(string.whitespace)
        if l == "":
            boards.append(BingoBoard.from_lines(rows))
            rows = []
            continue
        rows.append(l)
    if len(rows) > 0:
        boards.append(BingoBoard.from_lines(rows))

    for n in numbers:
        # print(f"--- {n} --- ")
        for b in boards:
            b.call_out(n)
            # print("---")
            # print_board(b)
            # breakpoint()
            if b.has_bingo():
                print(f"num: {n}")
                print(f"score: {b.score(n)}")
                print_board(b)
                sys.exit(0)
    print("E! No winners")
    sys.exit(1)
