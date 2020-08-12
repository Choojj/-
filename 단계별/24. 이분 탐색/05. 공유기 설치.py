import sys

N, C = map(int, sys.stdin.readline().split())
house_list = []
for _ in range(N):
    house_list.append(int(sys.stdin.readline()))

house_list.sort()

# print(N, C, house_list)

first = 1
last = house_list[-1] - house_list[0]
while (True):
    if (first > last):
        break

    mid = (first + last) // 2
    router_num = 1
    curr_house = house_list[0]
    for i in range(len(house_list)):
        if (curr_house + mid <= house_list[i]):
            router_num += 1
            curr_house = house_list[i]

    if (C > router_num):
        last = mid - 1
    if (C <= router_num):
        first = mid + 1
    
    # print(mid, router_num)

print(last)