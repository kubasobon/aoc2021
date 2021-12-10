import string

chunks = "()[]{}<>"
score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def validate_line(line):
    q = []
    for symbol in line:
        idx = chunks.find(symbol)
        assert idx != -1
        is_opening_brace = idx % 2 == 0

        if is_opening_brace:
            q.append(symbol)
            continue

        last_opening_brace = None
        try:
            last_opening_brace = q[-1]
            q = q[:-1]
        except IndexError:
            return False, symbol

        opening_idx = chunks.find(last_opening_brace)
        if opening_idx + 1 != idx:
            return False, symbol
    return True, ""


if __name__ == "__main__":
    data = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    total = 0
    for line in data:
        is_valid, symbol = validate_line(line)
        if is_valid:
            continue
        total += score[symbol]
    print(f"Total score: {total}")
