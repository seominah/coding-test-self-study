import sys
input = sys.stdin.readline

# a, b, c = map(int, input().rstrip())
a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

arr = [0] * 10
multi = list(map(int, str(a * b * c)))

for i in range(len(multi)) :
    arr[multi[i]] += 1

for i in arr :
    print(i)