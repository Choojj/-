"""
8 7 6 5 4 3 2 1 

1 2 3 4


1 2
4 3

1 2 5 6
4 3

1 2 5
4 3 6

1 2 5 7 8
4 3 6

4 3 6 8 7 5 2 1
"""

import sys

n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

sequence = [i + 1 for i in range(n)]
stack = []
push_pop = []
while (num_list):
    if (not sequence and stack[-1] != num_list[0]):
        push_pop = ["NO"]
        break

    if (not stack):
        stack.append(sequence.pop(0))
        push_pop.append("+")
    
    if (stack[-1] == num_list[0]):
        stack.pop()
        push_pop.append("-")
        num_list.pop(0)
    else:
        stack.append(sequence.pop(0))
        push_pop.append("+")

for i in push_pop:
    print(i)