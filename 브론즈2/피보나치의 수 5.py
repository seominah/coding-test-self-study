import sys
input = sys.stdin.readline

a = int(input())

a0 = 0
a1 = 1
an = 0

while a >= 0:
    if a < 2:
        an = a
        break
    elif a == 2:
        an = a0 + a1
        break
    else:
        an = a0 + a1
        a0 = a1
        a1 = an
    a -= 1

print(an)
