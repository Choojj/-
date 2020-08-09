"""
식이 최소값 -> -부분이 제일 크도록 괄호를 넣어주기

048-4035+1205+0154

5-4+6-2
"""

import sys

expression = sys.stdin.readline().rstrip().split("-")

# print(expression)

result = []
for i in range(len(expression)):
    temp = list(map(int, expression[i].split("+")))
    result.append(temp)
# print(result)

for i in range(len(result)):
    if (i == 0):
        minimal = sum(result[i])
    else:
        minimal -= sum(result[i])

print(minimal)