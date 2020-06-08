import sys

board = []

N = int(sys.stdin.readline().rstrip())

num = 666

while (N != 0):
	for i in range(len(str(num)) - 2):
		if (str(num)[i] == "6" and str(num)[i + 1] == "6" and str(num)[i + 2] == "6"):
			N -= 1
			break
	num += 1

print(num - 1)