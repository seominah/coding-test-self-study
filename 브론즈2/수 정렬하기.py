import sys
input = sys.stdin.readline

a = int(input().rstrip())
li = [int(input().rstrip()) for i in range(a)]

li.sort()

for i in li:
    print(i)

