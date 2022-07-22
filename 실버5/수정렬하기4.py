import sys
input = sys.stdin.readline

num = int(input().rstrip())
temp = []

for _ in range(num) :
    temp.append(int(input().rstrip()))

temp = sorted(temp, reverse=True)

for e in temp :
    print(e)

'''
1. _list.sort()
 - 리스트 끝에 사옹
 - 반환값 X, 자체 _list에서 정렬이 됨 

2. sorted(_list)
 - 파라미터에 리스트를 받음 
 - 정렬된 애들을 return 해줌

'''