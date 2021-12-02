import string


class Sub:
    def __init__(self, h, v):
        assert isinstance(h, int)
        assert isinstance(v, int)
        self.h = h
        self.v = v

    def parse(self, command_lines):
        commands = {
            "forward": self.forward,
            "up": self.up,
            "down": self.down,
        }
        for l in command_lines:
            l = l.strip(string.whitespace)
            cmd, str_n = l.split(" ")
            commands[cmd](int(str_n))

    def forward(self, n):
        self.h += n

    def up(self, n):
        self.v -= n

    def down(self, n):
        self.v += n

    def position(self):
        return self.h * self.v


if __name__ == "__main__":
    s = Sub(0, 0)
    with open("input.txt") as f:
        data = f.readlines()
    s.parse(data)
    print(f"Sub's position is {s.position}")
