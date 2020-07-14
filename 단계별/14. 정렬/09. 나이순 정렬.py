import sys

N = int(sys.stdin.readline().rstrip())

member_list = []

for i in range(N):
    member_age, member_name = sys.stdin.readline().rstrip().split()
    member_age, member_name = int(member_age), member_name
    member_list.append([member_age, member_name])

member_list.sort(key = lambda item : item[0])

for i in range(N):
    print(member_list[i][0], member_list[i][1])