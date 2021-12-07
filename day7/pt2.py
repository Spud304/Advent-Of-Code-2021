import os
import math

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

data = [int(x) for x in open(filename).read().split(',')]

# Iterate through data, find mean num
def find_mean(data):
    mean = 0
    for i in data:
        mean += i
    return math.floor(mean / len(data))

def find_steps(data):
    fuel = 0
    mean = find_mean(data)
    for step in range(len(data)):
        diff = abs(data[step] - mean)
        for i in range(diff):
            fuel += i + 1
    return fuel

print(find_mean(data))
print(find_steps(data))