import sys

time = 0

word = sys.stdin.readline().rstrip()

for i in word:
    if ("A" <= i <= "C"):
        time += 3
    elif ("D" <= i <= "F"):
        time += 4
    elif ("G" <= i <= "I"):
        time += 5
    elif ("J" <= i <= "L"):
        time += 6
    elif ("M" <= i <= "O"):
        time += 7
    elif ("P" <= i <= "S"):
        time += 8
    elif ("T" <= i <= "V"):
        time += 9
    elif ("W" <= i <= "Z"):
        time += 10

print(time)