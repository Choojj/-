import sys
import operator

N = int(sys.stdin.readline().rstrip())

location_list = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    location_list.append([x, y])

location_list.sort(key = operator.itemgetter(0))
location_list.sort(key = operator.itemgetter(1))
for i in location_list:
    print(i[0], i[1])