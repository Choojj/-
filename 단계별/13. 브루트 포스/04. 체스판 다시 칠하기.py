import sys

board = []

N, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(N):
	board.append(list(sys.stdin.readline().rstrip()))

min_count = float("inf")

for i in range(N - 8 + 1):
	for j in range(M - 8 + 1):
		count = 0
		for k in range(i, i + 8):
			for l in range(j, j + 8):
				if ((k + l) % 2 == 0 and board[k][l] != "W"):
					count += 1
					
				elif ((k + l) % 2 != 0 and board[k][l] != "B"):
					count += 1
		if (count > 32):
			count = 64 - count

		if (min_count > count):
			min_count = count

print(min_count)