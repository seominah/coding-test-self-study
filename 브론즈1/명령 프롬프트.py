import sys
input = sys.stdin.readline

name_list = []

for i in range(int(input().rstrip())):
    name_list.append(list(input().rstrip()))

P = name_list[0]

for i in range(1, len(name_list)):
    for j in range(len(P)):
        if P[j] != name_list[i][j]:
            P[j] = '?'

print("".join(P))