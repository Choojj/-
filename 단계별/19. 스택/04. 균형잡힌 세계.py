import sys

while (True):
    raw = sys.stdin.readline().rstrip()
    if (raw == "."):
        break

    datas = []
    curr_num = 0
    trig = False
    for i in range(len(raw)):
        if (raw[i] == "[" or raw[i] == "("):
            datas.append(raw[i])
            curr_num += 1
        elif (raw[i] == "]"):
            if (curr_num == 0):
                trig = True
                break

            if (datas[curr_num - 1] == "["):
                datas.pop()
                curr_num -= 1
            else:
                trig = True
                break
        elif (raw[i] == ")"):
            if (curr_num == 0):
                trig = True
                break
            
            if (datas[curr_num - 1] == "("):
                datas.pop()
                curr_num -= 1
            else:
                trig = True
                break

    if (curr_num == 0 and not trig):
        print("yes")
    else:
        print("no")