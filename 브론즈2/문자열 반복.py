import sys
input = sys.stdin.readline

a = int(input().rstrip())
str_list = []
for i in range(a):
    a = input().rstrip()
    str_list.append(a)

for char in str_list:
    result = ''
    f, s = char.split(' ')
    for i in s:
        result += i * int(f)
    print(result)
