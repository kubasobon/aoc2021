import string

chunks = "()[]{}<>"
score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
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
            return False, None

        opening_idx = chunks.find(last_opening_brace)
        if opening_idx + 1 != idx:
            return False, None
    return True, q


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
    line_score = []
    for line in data:
        is_valid, finisher = validate_line(line)
        if not is_valid:
            continue
        total = 0
        for brace in finisher[::-1]:
            total = 5 * total + score[brace]
        line_score.append(total)
    line_score.sort()
    print(line_score)
    print(f"Middle score: {line_score[round(len(line_score)/2)]}")
