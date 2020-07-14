import sys

T = int(sys.stdin.readline())

for i in range(T):
    data = sys.stdin.readline().rstrip()

    count = 0
    trig = True
    for i in range(len(data)):
        if (count == 0 and data[i] == ")"):
            trig = False

        if (data[i] == "("):
            count += 1
        elif (data[i] == ")"):
            count -= 1
        
    if (count == 0 and trig):
        print("YES")
    else:
        print("NO")