num_increase = 0

with open("./day1/input.txt", "r") as f:
    prevline = 0
    for line in f.read().split("\n"):
        if prevline == 0:
            prevline = int(line)
            continue
        line = int(line)
        if line > prevline:
            num_increase += 1
        prevline = line

print(num_increase)