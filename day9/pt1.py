import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

ll = [[int(y) for y in x] for x in open(filename).read().strip().split('\n')]
s=0
for i in range(len(ll)):
	for j in range(len(ll[0])):
		if i>0 and ll[i][j] >= ll[i-1][j]:
			continue
		if i<len(ll)-1 and ll[i][j] >= ll[i+1][j]:
			continue
		if j>0 and ll[i][j] >= ll[i][j-1]:
			continue
		if j<len(ll[0])-1 and ll[i][j] >= ll[i][j+1]:
			continue
		s += ll[i][j]+1
print(s)