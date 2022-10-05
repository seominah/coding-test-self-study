import sys
input = sys.stdin.readline

init_list = []
for i in range(20):
    init_list.append(i+1)

for i in range(10):
    a, b = map(int, input().rstrip().split(' '))
    while a < b:
        # temp = init_list[a-1]
        # init_list[a-1] = init_list[b-1]
        # init_list[b-1] = temp
        init_list[a-1], init_list[b-1] = init_list[b-1], init_list[a-1]
        a += 1
        b -= 1

print(' '.join(map(str, init_list)))
