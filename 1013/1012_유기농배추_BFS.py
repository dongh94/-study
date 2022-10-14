import sys
sys.stdin=open("1012_유기농배추.txt")
from collections import deque
#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#BFS : 1 영역의 모든 구역을 0으로 바꿔주면서~
def BFS(r, c):
    Q = deque([(r, c)])
    while Q:
        cr, cc = Q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                Q.append((nr,nc))
    return 1

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

    # BFS를 돌리며 count 한다.
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                cnt += BFS(r, c)
    print(cnt)
