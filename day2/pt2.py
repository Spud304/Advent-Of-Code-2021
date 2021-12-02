import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

aim = 0
horizontal = 0
depth = 0

with open(filename, "r") as f:
    data = f.read().split("\n")
    for line in data:
        if "forward" in line:
            trash, num = line.split(" ")
            horizontal += int(num)
            depth += (aim * int(num))
        if "up" in line:
            trash, num = line.split(" ")
            aim -= int(num)
        if "down" in line:
            trash, num = line.split(" ")
            aim += int(num)

print(horizontal, depth)
print(horizontal * depth)