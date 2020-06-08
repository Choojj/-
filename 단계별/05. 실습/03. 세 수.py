import sys

first_max = -float("inf")
second_max = -float("inf")

A, B, C = map(int, sys.stdin.readline().split())

num_list = [A, B, C]

for num in num_list:
    if (num >= first_max):
        second_max = first_max
        first_max = num
    elif (second_max < num < first_max):
        second_max = num

print(second_max)