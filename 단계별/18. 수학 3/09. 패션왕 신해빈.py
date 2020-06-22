import sys

N = int(sys.stdin.readline())

for i in range(N):
    costume_num = int(sys.stdin.readline())

    costume_list = []
    for j in range(costume_num):
        _, costume_type = sys.stdin.readline().rstrip().split(" ")
        print(costume_type)

        trig = True
        for k in range(len(costume_list)):
            if(costume_type == costume_list[k][1]):
                costume_list[k][0] += 1
                trig = False

        if (trig == True):
            costume_list.append([1, costume_type])

    print(costume_list)
