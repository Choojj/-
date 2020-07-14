import sys

def get_non_self_number(num):
    non_self_number = num

    while (num != 0):
        non_self_number += num % 10
        num //= 10
    
    return non_self_number

N = int(sys.stdin.readline().rstrip())

trig = False

for i in range(N):
    if (get_non_self_number(i) == N):
        print(i)
        trig = True
        break

if (trig == False):
    print(0)