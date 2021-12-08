import string


def build_translator(pattern_definitions):
    table = {}
    # sort by pattern length ascending
    pattern_definitions = sorted(pattern_definitions, key=lambda x: -len(x))
    pattern_1 = None
    pattern_4 = None
    pattern_7 = None
    for p in pattern_definitions:
        p = "".join(sorted(p))
        if len(p) == 2:
            table[p] = 1
        elif len(p) == 3:
            table[p] = 7
            pattern_7 = p
        elif len(p) == 4:
            table[p] = 4
            pattern_4 = 4
        elif len(p) == 5:
            if all(ch in pattern_1 for ch in p):
                table[p] = 3
            remaining = [ch for ch in p if ch not in pattern_7 and ch not in pattern_4]
            if len(remaining) == 1:
                table[p] = 5
            elif len(remaining) == 2:
                table[p] = 2
            else:
                raise ValueError(f"Could not map '{p}'")
        elif len(p) == 6:
            if all(ch in pattern_7 for ch in p):
                table[p] = 9
            else:
                table[p] = 6
        elif len(p) == 7:
            table[p] = 8
        else:
            raise ValueError(f"Could not map '{p}'")

    def translate(display):
        total = 0
        for d in display:
            d = "".join(sorted(d))
            if d in table:
                total += 1
        return total

    return translate


if __name__ == "__main__":
    with open("test_input.txt") as f:
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
