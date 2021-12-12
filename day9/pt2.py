from collections import Counter
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.txt')

data = [[int(y) for y in x] for x in open(filename).read().strip().split('\n')]

def basin(x,y):
	downhill = None
	for (dx, dy) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
		if dx in range(len(data)) and dy in range(len(data[0])):
			if data[x][y] > data[dx][dy]:
				downhill = (dx, dy)
	if downhill is None:
		return (x, y)
	thing = basin(*downhill)
	return thing

basins = []
for x in range(len(data)):
	for y in range(len(data[0])):
		if data[x][y] != 9:
			basins.append(basin(x, y))

thing = 1
for basin, common in Counter(basins).most_common(3):
	print(basin, common)
	thing *= common
print(thing)