import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    test_list = list(map(int, sys.stdin.readline().split()))

    priority_list = []
    for i in range(N):
        priority_list.append([test_list[i], i])

    count = 0
    while (len(priority_list) > 0):

        push_trig = False
        for i in range(len(priority_list)):
            if (priority_list[i][0] > priority_list[0][0]):
                priority_list.append(priority_list[0])
                priority_list.pop(0)
                push_trig = True
                break
        
        if (not push_trig):
            count += 1

            if (priority_list[0][1] == M):
                print(count)
                break

            priority_list.pop(0)
