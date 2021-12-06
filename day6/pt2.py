from collections import defaultdict, Counter
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

def doit():
    data = open(filename).read().split(',')
    data = [int(x) for x in data]
    data = Counter(data)
    for i in range(256):
        default = defaultdict(int)
        for k, v in data.items():
            if k == 0:
                default[6] += v
                default[8] += v
            else:
                default[k-1] += v
        data = default
    return sum(data.values())

print(doit())