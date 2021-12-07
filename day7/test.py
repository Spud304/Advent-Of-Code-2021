import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

data = [int(x) for x in open(filename).read().split(',')]

y1 = data[0]
y2 = data[1]
y3 = data[2]

mat = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
inv = np.linalg.inv(mat)
first3 = np.array([[y1, y2, y3]])
print(inv * first3)