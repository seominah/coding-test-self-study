import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    k = int(input().rstrip())  # 1
    n = int(input().rstrip())  # 3

    graph = [[1] * n for _ in range(k + 1)]
    # base = [ (num + 1) * 1 for num in range(n) ]

    i = 0
    for col in range(n):
        graph[0][col] = i

    for i in range(1, k + 1):
        for j in range(1, n):
            graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    print(graph[k][n - 1])

