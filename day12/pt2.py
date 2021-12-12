import os
from collections import defaultdict

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

data = [x for x in open(filename).read().strip().split('\n')]
# print(data)

edges = defaultdict(list)
for line in data:
	x, y = line.split("-")
	edges[x].append(y)
	edges[y].append(x)


def find_all_lines_to_end(current, visited, small2):
    if current == 'end':
            return 1
    c = 0
    for next_point in edges[current]:
        if next_point == 'start':
            continue
        if next_point.islower() and next_point != 'end':
            if next_point in visited:
                if not small2:
                    c += find_all_lines_to_end(next_point, visited, True)
            else:
                c += find_all_lines_to_end(next_point, visited | set([next_point]), small2)
        else:
            c += find_all_lines_to_end(next_point, visited, small2)
    return c

print(find_all_lines_to_end('start', set(), False))
