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
        tempFuel = 0
        diff = abs(data[step] - mean)
        for i in range(diff):
            # print(f'{step} {i}')
            tempFuel += i + 1
        print(f'Step {step}, Data: {data[step]}, diff: {diff}, fuel: {tempFuel}')
        fuel += tempFuel
    return fuel

print(find_mean(data))
print(find_steps(data))