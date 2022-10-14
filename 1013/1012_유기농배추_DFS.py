import sys
sys.stdin=open("1012_유기농배추.txt")
sys.setrecursionlimit(10000)
#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#DFS : 1을 찾아가면서 0으로 다 바꾸는 (이차원)
def DFS(r, c):
    arr[r][c] = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]:
            arr[nr][nc] = 0
            DFS(nr, nc)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 0의 이차원 그래프를 만든다.
    arr = [[0]*M for _ in range(N)]
    cnt = 0

    # 입력값으로 1을 채운다.
    for k in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    # DFS를 돌리며 돌린 기준으로 count 한다.
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
                DFS(r, c)
    print(cnt)