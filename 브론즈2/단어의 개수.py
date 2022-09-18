import sys
input = sys.stdin.readline

str = input().rstrip()

str_list = str.split(' ')
while '' in str_list :
    str_list.remove('')

print(len(str_list))
