import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(input().rstrip())


for i in li :
  target = list(i)
  score = 0
  result = 0
  for t in target :
    if t == 'O' :
      score = score + 1
      result = result + score
    else :
      score = 0
  print(result)
