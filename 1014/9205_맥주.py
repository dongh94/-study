import sys
sys.stdin=open("9205_맥주.txt")
from collections import deque

def BFS(sx, sy):
    Q = deque([(sx, sy)])
    while Q:
        x, y = Q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            return "happy"
        for d in range(n):
            if not v[d]:
                nx, ny = carr[d]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    v[d] = 1
                    Q.append((nx,ny))
    return "sad"

T = int(input())
for _ in range(T):
    #편의점 개수 & 좌표: 상근이네 집/ 편의점/ 페스티벌
    n = int(input())
    hx, hy = map(int, input().split())
    carr = []
    for _ in range(n):
        cx, cy = map(int, input().split())
        carr.append((cx, cy))
    fx, fy = map(int, input().split())
    v = [0]*(n+1)
    answer = BFS(hx, hy)
    print(answer)

    #기준은 50미터 / 20병
