import sys
input = sys.stdin.readline

a = input().rstrip()
li = list(a.upper())
start = 64
total_time = 0

for i in li:
    if start < ord(i) < start + 4:
        total_time += 3
    elif start + 3 < ord (i) < start + 7:
        total_time += 4
    elif start + 6 < ord(i) < start + 10:
        total_time += 5
    elif start + 9 < ord(i) < start + 13:
        total_time += 6
    elif start + 12 < ord(i) < start + 16:
        total_time += 7
    elif start + 15 < ord(i) < start + 20:
        total_time += 8
    elif start + 19 < ord(i) < start + 23:
        total_time += 9
    else:
        total_time += 10

print(total_time)