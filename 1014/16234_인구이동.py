import sys
sys.stdin = open("16234_인구이동.txt")
from collections import deque
#우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
#인구 배열
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 우하좌상 다 확인해서 방문 > 전체 값 / 연합 수 > 하루지남.
def BFS(sr, sc):
    Q = deque([(sr,sc)])
    visit[sr][sc] = 1
    U = deque([(sr,sc)])
    total = arr[sr][sc]
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue;
            if not visit[nr][nc] and R >= abs(arr[r][c] - arr[nr][nc]) >= L:
                visit[nr][nc] = 1
                Q.append((nr, nc))
                U.append((nr, nc))
                total += arr[nr][nc]
    # 인원수 갱신
    for ur, uc in U:
        arr[ur][uc] = total // len(U)

    return len(U)

answer = 0
while True:
    #하루마다 방문기록 다름.
    visit = list([0] * N for _ in range(N))
    move = False

    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                result = BFS(r, c)
                if result > 1:
                    move = True
    #이동하지 않으면
    if not move: break;
    #이동했으면
    answer += 1
print(answer)
