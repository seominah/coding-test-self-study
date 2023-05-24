import sys
from datetime import datetime

input = sys.stdin.readline

a, b = map(int, input().split(' '))

print(datetime.strftime(datetime(2007, a, b), '%A')[:3].upper())