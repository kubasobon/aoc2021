import string
from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=2000)
def step_cost(n):
    return sum(range(n + 1))


def align_crab_subs(crab_subs):
    c = Counter(crab_subs)
    cost_per_position = Counter()
    for position in range(min(c.keys()), max(c.keys()) + 1):
        cost = 0
        for crab_position, count in c.items():
            cost += step_cost(abs(position - crab_position)) * count
        cost_per_position[position] = cost
    # lowest cost position
    return cost_per_position.most_common()[-1]


if __name__ == "__main__":
    test_data = "16,1,2,0,4,2,7,1,2,14"
    with open("input.txt") as f:
        data = f.readline()
    crab_subs = [int(x) for x in data.strip(string.whitespace).split(",")]
    position, cost = align_crab_subs(crab_subs)
    print(f"Aligning crab submarines at {position} is the cheapest:")
    print(f"{cost} fuel units")
