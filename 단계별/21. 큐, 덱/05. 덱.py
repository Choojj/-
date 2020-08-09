import sys

N = int(sys.stdin.readline())

deck = []
for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    
    if (command[0] == "push_front"):
        deck.insert(0, command[1])

    elif (command[0] == "push_back"):
        deck.append(command[1])

    elif (command[0] == "pop_front"):
        if (deck):
            print(deck[0])
            deck.pop(0)
        else:
            print(-1)
    
    elif (command[0] == "pop_back"):
        if (deck):
            print(deck[-1])
            deck.pop()
        else:
            print(-1)
    
    elif (command[0] == "size"):
        print(len(deck))
    
    elif (command[0] == "empty"):
        if (deck):
            print(0)
        else:
            print(1)

    elif (command[0] == "front"):    
        if (deck):
            print(deck[0])
        else:
            print(-1)
    
    elif (command[0] == "back"):
        if (deck):
            print(deck[-1])
        else:
            print(-1)