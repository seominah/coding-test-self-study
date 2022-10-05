import sys
input = sys.stdin.readline

num = int(input().rstrip())

init_list = []
result = ''
for i in range(num):
    init_list.append(input().rstrip())

for i in range(num):
    a = init_list[i][::-1]
    for i in range(num):
        if (a == init_list[i]):
            result = a

print(len(result), result[len(result)//2])