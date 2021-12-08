import string


def build_translator(pattern_definitions):
    table = {}
    # sort by pattern length ascending
    pattern_definitions = sorted(pattern_definitions, key=lambda x: len(x))
    pattern_1 = None
    pattern_4 = None
    pattern_7 = None
    for p in pattern_definitions:
        p = "".join(sorted(p))
        if len(p) == 2:
            table[p] = 1
            pattern_1 = p
        elif len(p) == 3:
            table[p] = 7
            pattern_7 = p
        elif len(p) == 4:
            table[p] = 4
            pattern_4 = p
        elif len(p) == 5:
            if all(ch in p for ch in pattern_1):
                table[p] = 3
                continue
            remaining = [ch for ch in p if ch not in pattern_7 and ch not in pattern_4]
            if len(remaining) == 1:
                table[p] = 5
            elif len(remaining) == 2:
                table[p] = 2
            else:
                raise ValueError(f"Could not map '{p}'")
        elif len(p) == 6:
            if all(ch in p for ch in pattern_7):
                if all(ch in p for ch in pattern_4):
                    table[p] = 9
                else:
                    table[p] = 0
            else:
                table[p] = 6
        elif len(p) == 7:
            table[p] = 8
        else:
            raise ValueError(f"Could not map '{p}'")

    def translate(display):
        decoded = ""
        for d in display:
            d = "".join(sorted(d))
            decoded += str(table[d])
        return decoded

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
        total += int(out)
    print(total)
