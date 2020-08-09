import sys
import math

N = int(sys.stdin.readline())

ring_radius_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    gcd = math.gcd(ring_radius_list[0], ring_radius_list[i])
    print(f"{int(ring_radius_list[0] / gcd)}/{int(ring_radius_list[i] / gcd)}")