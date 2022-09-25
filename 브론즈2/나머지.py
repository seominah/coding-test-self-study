import sys
input = sys.stdin.readline


num_list = []
for i in range(10) :
    a = int(input().rstrip())
    num_list.append(a)

result = set([])
for num in num_list :
    result.add(num % 42)

print(len(result))