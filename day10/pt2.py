import os
from collections import deque
from statistics import median

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

#Line 3, Line 5, Line 6, Line 8, Line 9

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

data = [x for x in open(filename, 'r').read().splitlines()]
totalPoints = list()

def test(l):
    line = deque()
    for i, c in enumerate(l):
        if c in pairs.keys():
            line.appendleft(pairs[c])
        elif c != line[0]:
            print(f'Corruption at line {i}, char {c}')
            return 0
        elif c == line[0]:
            line.popleft()

    closingPoints = 0
    for c in line:
       closingPoints *= 5
       closingPoints += points[c] 

    return closingPoints

for line in data:
    # print(f'Line {line}')
    # totalPoints.append(test(line))
    line = test(line)
    if line > 0:
        totalPoints.append(line)

print(totalPoints)
print(median(totalPoints))