import sys
input = sys.stdin.readline

result = []

for _ in range(9):
    int(result.append(input().rstrip()))

print(max(result))
print(result.index(max(result))+1)