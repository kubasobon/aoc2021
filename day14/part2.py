import string
import collections


def parse_rules(lines):
    return {pair: infix for pair, infix in (l.split(" -> ") for l in lines)}


def process_once(template, rules):
    new_template = []
    for i in range(1, len(template), 1):
        pair = template[i - 1 : i + 1]
        new_template.append(pair[0])
        new_template.append(rules[pair])
        # print(pair)
        # print(new_template)
        # breakpoint()
    new_template.append(template[-1])
    return "".join(new_template)


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
    template = data[0]
    rules = parse_rules(data[2:])
    print(f"Template: {template}")
    for i in range(25):
        template = process_once(template, rules)
        # print(f"After step {i+1}: {template}")
    print(f"Template length after step {i+1}: {len(template)}")
    mc = collections.Counter(template).most_common()
    print(f"Most common: '{mc[0][0]}'={mc[0][1]}")
    print(f"Least common: '{mc[-1][0]}'={mc[-1][1]}")
    print(f"Result: {mc[0][1] - mc[-1][1]}")
