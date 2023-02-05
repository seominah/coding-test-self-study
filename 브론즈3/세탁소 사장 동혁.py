import sys
input = sys.stdin.readline

num = int(input().rstrip())
T_list = []
result = [0, 0, 0, 0]

for i in range(num):
    T_list.append(int(input().rstrip()))


for i in range(num):
    T = T_list[i]

    while T > 0:
        result[0] = T // 25
        T = T % 25

        result[1] = T // 10
        T = T % 10

        result[2] = T // 5
        T = T % 5

        result[3] = T // 1
        T = T % 1

    print(" ".join(map(str, result)))