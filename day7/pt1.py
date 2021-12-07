import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

data = [int(x) for x in open(filename).read().split(',')]

# iterate through data find median number
def find_median(data):
    data.sort()
    return data[int(len(data)/2)]

# iterate and find difference between median and number in data
def find_difference(data):
    med = find_median(data)
    fuel = 0
    for i in data:
        if med != i:
            fuel += abs(i - med)
    return fuel

print(find_median(data))
print(find_difference(data))