import string
import collections

def parse_template(template):
    pairs = (template[i-1:i+1] for i in range(1, len(template)))
    return collections.Counter(pairs)

def parse_rules(lines):
    return {pair: infix for pair, infix in (l.split(" -> ") for l in lines)}


def process_once(pairs, rules):
    new_pairs = collections.Counter()
    for pair, count in pairs.items():
        infix = rules[pair]
        a, b = pair[0], pair[1]
        new_pairs[a+infix] += count
        new_pairs[infix+b] += count
    return new_pairs

def count_letters(template, pairs):
    letters = collections.Counter()
    for pair, count in pairs.items():
        a, b = pair[0], pair[1]
        letters[a] += count
        letters[b] += count
    true_count = collections.Counter()
    for letter, count in letters.items():
        if template[0] == letter or template[-1] == letter:
           count += 1
        true_count[letter] = int(count/2)
    return true_count.most_common()


if __name__ == "__main__":
    test_data = [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]

    with open("input.txt") as f:
        data = [l.strip(string.whitespace) for l in f]
    data = test_data
    pairs = parse_template(data[0])
    rules = parse_rules(data[2:])
    print(f"Template: {pairs}")

    for i in range(10):
        pairs = process_once(pairs, rules)

    mc = count_letters(data[0], pairs)
    print(f"Most common: '{mc[0][0]}'={mc[0][1]}")
    print(f"Least common: '{mc[-1][0]}'={mc[-1][1]}")
    print(f"Result: {mc[0][1] - mc[-1][1]}")
