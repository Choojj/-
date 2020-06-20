import sys

alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter_check = []

group_word = True

count = 0

for i in range(26):
    letter_check.append(False)

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    word = sys.stdin.readline().rstrip()

    if (len(word) > 1):
        for j in range(len(word) - 1):
            if (word[j] != word[j + 1]):
                if (letter_check[ord(word[j]) - 97] == True):
                    group_word = False
                letter_check[ord(word[j]) - 97] = True

        if (letter_check[ord(word[len(word) - 1]) - 97] == True):
            group_word = False
        letter_check[ord(word[len(word) - 1]) - 97] = True

    if (group_word == True):
        count += 1
    
    group_word = True

    for i in range(26):
        letter_check[i] = False

print(count)