import sys
input = sys.stdin.readline

T = int(input())

A = 300
B = 60
C = 10

result = [0, 0, 0]

while T > 0:
    if T % 10 != 0:
        print(-1)
        break
    if T >= A:
        result[0] = T // A
        T = T % A
    if T >= B:
        result[1] = T // B
        T = T % B
    # if T >= 10:
    result[2] = T // C
    print(" ".join(map(str, result)))
    T = T % C
