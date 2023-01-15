import sys
input = sys.stdin.readline

a = input().rstrip()
print(a)
b = list(map(int, input().rstrip().split()))
print(min(b), max(b))
