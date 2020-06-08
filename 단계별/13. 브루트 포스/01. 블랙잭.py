import sys

black_jack = -float("inf")

N, M = map(int, sys.stdin.readline().rstrip().split())
card_list = list(map(int, sys.stdin.readline().rstrip().split()))

trig1 = False
trig2 = False

for i in range(0, N - 2):
    if (trig1 == True):
        break
    for j in range(i + 1, N - 1):
        if (trig2 == True):
            break
        for k in range(j + 1, N):
            if (card_list[i] + card_list[j] + card_list[k] == M):
                black_jack = card_list[i] + card_list[j] + card_list[k]
                trig1 = True
                trig2 = True
                break
            elif (black_jack < card_list[i] + card_list[j] + card_list[k] <= M):
                black_jack = card_list[i] + card_list[j] + card_list[k]

print(black_jack)