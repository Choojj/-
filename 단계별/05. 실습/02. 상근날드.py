import sys

min_burger = float("inf")
min_coke = float("inf")

for i in range(5):
    price = int(sys.stdin.readline())
    if (i < 3):
        if (price < min_burger):
            min_burger = price

    else:
        if (price < min_coke):
            min_coke = price

print(min_burger + min_coke - 50)