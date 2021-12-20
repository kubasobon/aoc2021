from collections import Counter


def pair_levels(l, lvl):
    c = Counter()
    c[lvl] += 1

    for sub_l in l:
        if isinstance(sub_l, int):
            continue
        sub_c = pair_levels(sub_l, lvl + 1)
        for k, v in sub_c.items():
            c[k] += v

    print(l, " @", lvl, ": ", c, flush=True)
    return c


def numbers(l):
    c = Counter()
    for sub_l in l:
        if isinstance(sub_l, int):
            c[sub_l] += 1
        else:
            sub_c = numbers(sub_l)
            for k, v in sub_c.items():
                c[k] += v
    return c


if __name__ == "__main__":
    data = "[[[[[9,8],1],2],3],4]"
    l = eval(data)
