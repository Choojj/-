import sys

multi = 1

multi_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(3):
    N = int(sys.stdin.readline())
    multi *= N

for i in range(len(str(multi))):
    if (multi % 10 == 0):
        multi_list[0] += 1
    elif (multi % 10 == 1):
        multi_list[1] += 1
    elif (multi % 10 == 2):
        multi_list[2] += 1
    elif (multi % 10 == 3):
        multi_list[3] += 1
    elif (multi % 10 == 4):
        multi_list[4] += 1
    elif (multi % 10 == 5):
        multi_list[5] += 1
    elif (multi % 10 == 6):
        multi_list[6] += 1
    elif (multi % 10 == 7):
        multi_list[7] += 1
    elif (multi % 10 == 8):
        multi_list[8] += 1
    else:
        multi_list[9] += 1

    multi //= 10

for i in range(10):
    print(multi_list[i])