import re
from collections import defaultdict
from collections import Counter

edges = [re.match(r"(\w+)-(\w+)", l).groups() for l in open("input12.txt")]
graph = defaultdict(set)
paths = list()
for edge in edges:
    node1, node2 = edge
    graph[node1].add(node2)
    graph[node2].add(node1)

print(graph)
print(edges)

def paths_to_end(start_node, path):
    global paths
    if start_node == "end":
        paths.append(path)
        return
    for neighbour in graph[start_node]:
        if (neighbour not in path or (neighbour in path and neighbour.isupper())):
            new_path = path[:]
            new_path.append(neighbour)
            paths_to_end(neighbour, new_path)

def check(node, path):
    if node == "start":
        return False
    if node not in path:
        return True
    if node.isupper():
        return True
    if not [n for n in path if n.islower() and path.count(n) > 1]:
        return True
    return False


def paths_to_end2(start_node, path):
    global paths
    if start_node == "end":
        paths.append(path)
        return
    for neighbour in graph[start_node]:
        if check(neighbour,path):
            new_path = path[:]
            new_path.append(neighbour)
            paths_to_end2(neighbour, new_path)

if __name__ == "__main__":
    
    paths_to_end2("start", ["start"])
    print(len(paths))