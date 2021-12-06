import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

with open(filename) as f:
    data = f.read().split(',')
    data = [int(x) for x in data]
    print(data)
    numAlreadyThere = len(data)
    for i in range(256):
        print(i)
        for i in range(len(data)):
            if data[i] >= 0:
                data[i] -= 1
            if data[i] < 0:
                data[i] = 6
                data.append(8)
            numAlreadyThere = len(data)

print(len(data))