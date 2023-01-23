import sys
input = sys.stdin.readline

a = list(map(int, input().split(' ')))
result = ''

for i in range(len(a) - 1):
    if abs(a[i] - a[i+1]) != 1:
        result = 'mixed'
        break
    elif a[i] - a[i+1] < 0:
        result = 'ascending'
    else:
        result = 'descending'

print(result)