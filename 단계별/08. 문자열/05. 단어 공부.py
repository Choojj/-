import sys

alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
word_count = []

count = 0

word = sys.stdin.readline().rstrip()

for i in alphabet_lower:
    word_count.append(word.count(i))

for i in enumerate(alphabet_upper):
    word_count[i[0]] += word.count(i[1])

for i in enumerate(word_count):
    if (i[1] == max(word_count)):
        count += 1
        max_letter = i[0]

if (count < 2):
    print(chr(max_letter + 65))
else:
    print("?")