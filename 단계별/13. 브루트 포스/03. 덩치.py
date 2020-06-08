import sys

weight_height = []

N = int(sys.stdin.readline().rstrip())

for i in range(N):
	x, y = map(int, sys.stdin.readline().rstrip().split())
	
	weight_height.append([x, y])

for i in range(N):
	count = 1

	for j in range(N):
		if (i != j):
			if (weight_height[i][0] < weight_height[j][0] and weight_height[i][1] < weight_height[j][1]):
				count += 1
	
	print(count)