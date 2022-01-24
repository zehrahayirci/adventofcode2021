import re
from collections import defaultdict

if __name__ == "__main__":



    regexp   = re.compile(r'-?\d+')
    commands = []
    fin= open("input22.txt", "r")
    for line in fin:
        on     = line.startswith('on') # True if the command is "on", False otherwise
        cuboid = tuple(map(int, regexp.findall(line)))
        commands.append((on, cuboid))

    on_cubes = set()
for on, (x1, x2, y1, y2, z1, z2) in commands:
    if on:
        for x in range(max(x1, -50), min(x2, 50) + 1):
            for y in range(max(y1, -50), min(y2, 50) + 1):
                for z in range(max(z1, -50), min(z2, 50) + 1):
                    on_cubes.add((x, y, z))
    else:
        for x in range(max(x1, -50), min(x2, 50) + 1):
            for y in range(max(y1, -50), min(y2, 50) + 1):
                for z in range(max(z1, -50), min(z2, 50) + 1):
                    on_cubes.discard((x, y, z))
    n_on = len(on_cubes)
print('Part 1:', n_on)