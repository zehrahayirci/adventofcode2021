from collections import defaultdict
import re


def iterate(iterations):
    pair_count = input_pair_count
    for _ in range(iterations):
        pair_count = update_pair_count(pair_count)
    alphabet_count = defaultdict(int)
    for pair in pair_count:
        alphabet_count[pair[0]] += pair_count[pair]
        alphabet_count[pair[1]] += pair_count[pair]
    print(alphabet_count)
    sorted_values = sorted(alphabet_count.values())
    print(sorted_values)
    print(int((sorted_values[-1] - sorted_values[0] + 1) / 2))


def update_pair_count(pair_count):
    new_pair_count = defaultdict(int)
    for pair in pair_count.keys():
        if pair in rules.keys():
            new_pair_count[pair[0] + rules[pair]] += pair_count[pair]
            new_pair_count[rules[pair] + pair[1]] += pair_count[pair]
        else:
            new_pair_count[pair] += pair_count[pair]
    return new_pair_count


if __name__ == "__main__":
    
    file1 = open("input14.txt", "r")
    input = file1.readline().strip()
    file1.readline()
    rules = {x: y for x, y in [re.match(r"(\w\w) -> (\w)", rule).groups() for rule in file1.readlines()]}
    input_pair_count = defaultdict(int)
    for idx in range(len(input) - 1):
        input_pair_count[input[idx:idx+2]] += 1
    lines = file1.read().split()


    iterate(40)
