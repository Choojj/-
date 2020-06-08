import sys

def get_non_self_number(num):
    non_self_number = num

    while (num != 0):
        non_self_number += num % 10
        num //= 10
    
    return non_self_number

self_number_type = []

for i in range(10000):
    self_number_type.append(True)

for i in range(1, 10000):
    if (self_number_type[i] == True):
        n = i
    while (get_non_self_number(n) < 10000):
        self_number_type[get_non_self_number(n)] = False

        n = get_non_self_number(n)

for i in range(1, 10000):
    if (self_number_type[i] == True):
        print(i)