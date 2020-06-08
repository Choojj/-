import sys

max_num = -float("inf")
max_num_order = 0

for i in range(9):
    num = int(sys.stdin.readline())
    if (num > max_num):
        max_num_order = i + 1
        max_num = num

print(max_num)
print(max_num_order)