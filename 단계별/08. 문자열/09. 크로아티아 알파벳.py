import sys

word = sys.stdin.readline().rstrip()

list_num = 0
word_num = 0

while (list_num < len(word)):
    if (word[list_num] == "c" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "="):
            word_num += 1
            list_num += 2
        elif (word[list_num + 1] == "-"):
            word_num += 1
            list_num += 2
        else:
            word_num += 1
            list_num += 1
    
    elif (word[list_num] == "d" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "-"):
            word_num += 1
            list_num += 2
        elif (word[list_num + 1] == "z" and len(word[list_num:]) >= 3):
            if (word[list_num + 2] == "="):
                word_num += 1
                list_num += 3
            else:
                word_num += 1
                list_num += 1
        else:
            word_num += 1
            list_num += 1
    
    elif (word[list_num] == "l" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "j"):
            word_num += 1
            list_num += 2
        else:
            word_num += 1
            list_num += 1

    elif (word[list_num] == "n" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "j"):
            word_num += 1
            list_num += 2
        else:
            word_num += 1
            list_num += 1

    elif (word[list_num] == "s" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "="):
            word_num += 1
            list_num += 2
        else:
            word_num += 1
            list_num += 1

    elif (word[list_num] == "z" and len(word[list_num:]) >= 2):
        if (word[list_num + 1] == "="):
            word_num += 1
            list_num += 2
        else:
            word_num += 1
            list_num += 1
    
    else:
        word_num += 1
        list_num += 1

print(word_num)