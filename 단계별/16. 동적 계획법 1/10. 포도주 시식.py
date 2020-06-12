"""
첫번재를 마시던가 두번째를 마시던가
첫번째잔 O -> 두번째잔 O -> 3번째잔 X
          -> 두번째잔 X -> 3번째잔...
두번째잔 O -> 세번째잔 O -> 4번째잔 X
          -> 세번째잔 X -> 4번째잔...

N = 6 -> 6 10 13 9 8 1
dp[0] = 0
dp[1] = 6
dp[2] = 6 + 10
dp[3] = max(6 + 10, 6 + 13, 10 + 13) = max(dp[2], dp[1] + 13, dp[0] + 10 + 13) = 10 + 13 = dp[0] + 10 + 13
dp[4] = max(6 + 10 + 9, 6 + 13 + 9, 10 + 13) = amx(dp[2] + 9, dp[1] + 13 + 9, dp[3]) = 6 + 13 + 9 = dp[1] + 13 + 9
dp[5] = max(6 + 10 + 9 + 8, 6 + 13 + 9, 10 + 13 + 8) = max(dp[2] + 9 + 8, dp[4], dp[3] + 8) = 6 + 10 + 9 + 8 = dp[2] + 9 + 8
dp[6] = max(6 + 10 + 9 + 8, 6 + 10 + 9 + 1, 6 + 10 + 8 + 1, 6 + 13 + 9 + 1, 6 + 13 + 8 + 1, 10 + 13 + 8 + 1, 10 + 9 + 8, 10 + 9 + 1)
      max(dp[5], dp[4] + 1, dp[3] + 8 + 1)

dp[n] = max(dp[n-1], dp[n-2] + N[n], dp[n-3] + N[n-1] + N[n])
"""

import sys

N = int(sys.stdin.readline())

wine_value = [0]
for i in range(N):
    wine_value.append(int(sys.stdin.readline()))

wine_sum = [0 for _ in range(N + 1)]

for i in range(N + 1):
    if (i == 0):
        wine_sum[i] = 0
    elif (i == 1):
        wine_sum[i] = wine_value[i]
    elif (i == 2):
        wine_sum[i] = wine_value[i] + wine_value[i - 1]
    else:
        wine_sum[i] = max(wine_sum[i - 1], wine_sum[i - 2] + wine_value[i], wine_sum[i - 3] + wine_value[i] + wine_value[i - 1])

print(wine_sum[-1])