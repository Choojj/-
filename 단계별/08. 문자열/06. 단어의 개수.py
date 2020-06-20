import sys

count = 0

sentence = sys.stdin.readline().rstrip()

for i in range(1, len(sentence) - 1):
    if (sentence[i] == " "):
        count += 1

if (sentence == ""):
    print(0)
elif (count == 0):
    print(1)
else:
    print(count + 1)