num1 = input()
num2 = input()

for i in range(len(num2) - 1, -1, -1):
    print(int(num1) * int(num2[i]))
print(int(num1) * int(num2))