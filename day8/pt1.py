import os
import re



here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.txt')


pattern = re.compile("(\|.*)")
data = re.findall(pattern, open(filename).read())
newData = []
for i in data:
    x = i.replace('|', '').strip()
    newData.append(x)

test = {
    'acedgfb': 8,
    'cdfbe' : 5,
    'gcdfa' : 2,
    'fbcad' : 3,
    'dab' : 7,
    'cefabd' : 9,
    'cdfgeb' : 6,
    'eafb' : 4,
    'cagedb' : 1,
    'ab' : 1
}

l = [2, 4, 3, 7]


def pt1(data):
    c = 0
    for i in range(len(data)):
        line = data[i].split(" ")
        for i in line:
            if len(i) in l:
                c += 1
    return c

# trash moved to test.py
def pt2(data):
    num = []
    shortNum = []
    for i in data:
        i = i.split(" ")
        print(i)
        for j in i:
            for k, v in test.items():
                if sorted(k) == sorted(j):
                    shortNum.append(v)
        num.append("".join([str(i) for i in shortNum]))
        shortNum = []
    return num

entry = ["cdfeb fcadb cdfeb cdbaf"]

# print(data)
print(pt1(newData))
print(pt2(entry))