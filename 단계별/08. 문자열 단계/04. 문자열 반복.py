import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    for j in range(len(S)):
        for k in range(int(R)):
            print(S[j], end = "")
    print()