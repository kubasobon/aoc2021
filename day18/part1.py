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

    #print(l, " @", lvl, ": ", c, flush=True)
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


def reduce(l):
    pair_cond = any(x >= 4 for x in pair_levels(l, 0))
    num_cond = any(x >= 10 for x in numbers(l))
    while pair_cond or num_cond:
        if pair_cond:
            l = explode_leftmost(l, 0)
        elif num_cond:
            l = split_leftmost(l)
        break
        pair_cond = any(x >= 4 for x in pair_levels(l, 0))
        num_cond = any(x >= 10 for x in numbers(l))
    return l

def explode_leftmost(l, lvl):
    left, right = l
    if isinstance(left, list):
        print(left, lvl+1)
        if lvl+1 < 4:
            explode_leftmost(left, lvl+1)
        else:
            left = 99
    l = [left, right]
    return l

if __name__ == "__main__":
    data = "[[[[[9,8],1],2],3],4]"
    l = eval(data)
    l = reduce(l)
    print(l)
