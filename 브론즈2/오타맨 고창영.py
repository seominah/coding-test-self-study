import sys
input = sys.stdin.readline

# a, b = input().rstrip().split(' ')
# print(b.replace(b[int(a)-1], ''))

n = int(input().strip())

for i in range(n):
    f, miss_str = input().rstrip().split(' ')
    miss_str = list(miss_str)
    miss_str.pop(int(f)-1)
    # print(f'f = {f}')
    # print(miss_str[int(f)-1])
    # result = miss_str.replace(miss_str[int(f)-1], '', 1)
    print(''.join(miss_str))