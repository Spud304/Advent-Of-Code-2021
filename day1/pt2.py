num_increase = 0
line_counter = 0

with open("./day1/input.txt", "r") as f:
    A = 0
    B = 0
    old_sum = 0
    for line in f.read().split("\n"):
        C = int(line)
        if line_counter == 0:
            A = C
            line_counter += 1
            continue
        if line_counter == 1:
            B = C
            line_counter += 1
            continue
        if A + B + C > old_sum and old_sum != 0:
            num_increase += 1
        old_sum = A + B + C
        A = B
        B = C

print(num_increase)