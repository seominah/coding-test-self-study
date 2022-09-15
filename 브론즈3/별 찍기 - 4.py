import sys

input = sys.stdin.readline

num = int(input().rstrip())
init = 0

for _ in range(num) :
    print(' ' * init + '*' * num)
    init += 1
    num -= 1
