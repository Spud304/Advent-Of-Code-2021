import os
from typing import Counter

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

l_dict = {}

with open(filename, 'r') as f:
    lines = f.read().split('\n')
    counter = 0
    for line in lines:
        l_dict[counter] = list(line)
        counter += 1

# find most common bit in the corresponding position of all numbers in the dictionary
def find_most_common_bit():
    bit_dict = {}
    for i in range(len(l_dict[0])):
        bit_dict[i] = []
        for j in range(len(l_dict)):
            bit_dict[i].append(l_dict[j][i])
    for i in range(len(l_dict[0])):
        bit_dict[i] = Counter(bit_dict[i])
        bit_dict[i] = bit_dict[i].most_common(1)[0][0]
    return bit_dict

def find_least_common_bit():
    bit_dict = {}
    for i in range(len(l_dict[0])):
        bit_dict[i] = []
        for j in range(len(l_dict)):
            bit_dict[i].append(l_dict[j][i])
    for i in range(len(l_dict[0])):
        bit_dict[i] = Counter(bit_dict[i])
        bit_dict[i] = bit_dict[i].most_common()[-1][0]
    return bit_dict

gamma = "".join(find_most_common_bit().values())
epislon = "".join(find_least_common_bit().values())

print(gamma)
print(int(gamma, 2))
print(epislon)
print(int(epislon, 2))

print(int(gamma, 2) * int(epislon, 2))