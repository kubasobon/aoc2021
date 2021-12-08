import string


def build_translator(pattern_definitions):
    table = {}
    for p in pattern_definitions:
        p = "".join(sorted(p))
        if len(p) == 2:
            table[p] = 1
        elif len(p) == 3:
            table[p] = 7
        elif len(p) == 4:
            table[p] = 4
        elif len(p) == 7:
            table[p] = 8

    def translate(display):
        total = 0
        for d in display:
            d = "".join(sorted(d))
            if d in table:
                total += 1
        return total

    return translate


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f.readlines()]
    total = 0
    for line in data:
        pattern_definitions, display = line.split(" | ")
        pattern_definitions = pattern_definitions.split()
        display = display.split()

        translate = build_translator(pattern_definitions)
        out = translate(display)
        total += out
    print(total)
