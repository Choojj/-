import sys

N = int(sys.stdin.readline().rstrip())

string_list = []

for i in range(N):
    string = sys.stdin.readline().rstrip()
    string_list.append(string)

string_list.sort(key = lambda item: (len(item), item))

print(string_list[0])
for i in range(len(string_list) - 1):
    if (string_list[i] != string_list[i + 1]):
        print(string_list[i + 1])