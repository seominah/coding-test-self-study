import sys

input = sys.stdin.readline

num = int(input().rstrip())
N = num
cycle = 0

while True:
    cycle += 1
    _sum = num // 10 + num % 10
    num = (num % 10) * 10 + _sum % 10
    if N == num:
        break

print(cycle)
