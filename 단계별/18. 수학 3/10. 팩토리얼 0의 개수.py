import sys, math

N = int(sys.stdin.readline())

factorial = list(str(math.factorial(N)))
factorial.reverse()

count = 0
for i in range(len(factorial)):
    if (factorial[i] == "0"):
        count += 1
    else:
        break

print(count)