import os
from collections import deque

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.txt')

#Line 3, Line 5, Line 6, Line 8, Line 9

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

data = [x for x in open(filename, 'r').read().splitlines()]

# print(data)
c = 1

totalPoints = list()

def test(l):
    line = deque()
    for i, c in enumerate(l):
        if c in pairs.keys():
            line.appendleft(pairs[c])
        elif c != line[0]:
            print(f'Corruption at line {i}, char {c}')
            return points[c]
        elif c == line[0]:
            line.popleft()
    return 0

for line in data:
    print(f'Line {line}')
    totalPoints.append(test(line))

print(sum(totalPoints))