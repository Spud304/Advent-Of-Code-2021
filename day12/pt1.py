import os
from collections import defaultdict

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

data = [x for x in open(filename).read().strip().split('\n')]
low = 'abcdefghijklmnopqrstuvwxyz'
# print(data)

edges = defaultdict(list)
for line in data:
	x, y = line.split("-")
	edges[x].append(y)
	edges[y].append(x)

# print(edges)

def issmall(c):
	return c != 'end' and c[0] in low

def find_all_lines_to_end(current, visited):
    if current == 'end':
            return 1
    c = 0
    for next_point in edges[current]:
        if next_point.islower() and next_point != 'end':
            if next_point not in visited:
                c += find_all_lines_to_end(next_point, visited | set([next_point]))
        else:
            c += find_all_lines_to_end(next_point, visited)
    return c

print(find_all_lines_to_end('start', set(['start'])))
