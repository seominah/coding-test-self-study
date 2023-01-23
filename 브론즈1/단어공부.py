import sys
input = sys.stdin.readline

a = list(input().rstrip().upper())
cnt = 1
char_dict = {}

for i in a:
    if i in char_dict:
        cnt = char_dict[i]
        cnt += 1
    char_dict[i] = cnt
    cnt = 1

result = list(char_dict.values())

print('?') if result.count(max(result)) > 1 else print(''.join([k for k, v in char_dict.items() if v == max(result)]))


