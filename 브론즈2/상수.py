import sys
input = sys.stdin.readline().rstrip()

a, b = map(int, input.split(" "))

num1 = (a % 10) * 100 + ((a % 100) // 10) * 10 + (a // 100)
num2 = (b % 10) * 100 + ((b % 100) // 10) * 10 + (b // 100)

print(num1) if num1 > num2 else print(num2)