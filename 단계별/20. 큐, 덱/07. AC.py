import sys

T = int(sys.stdin.readline())
for _ in range(T):
    command = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    num_list = list(sys.stdin.readline().strip()[1:-1].split(","))

    if (num_list[0] == ""):
        num_list = []

    reverse_trig = False
    error_trig = False
    for cmd in command:
        if (cmd == "R"):
            reverse_trig = not reverse_trig
        
        elif (cmd == "D"):
            if (num_list):
                if (reverse_trig):
                    num_list.pop()
                else:
                    num_list.pop(0)
            else:
                error_trig = True
                break

    if (error_trig):
        print("error")
    else:
        if (reverse_trig):
            num_list.reverse()

        print("[", end = "")
        for num in enumerate(num_list):
            if (num[0] == len(num_list) - 1):
                print(num[1], end = "")
            else:
                print(num[1] + ",", end = "")
        print("]")