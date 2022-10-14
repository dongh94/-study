import sys
sys.stdin=open("1697_숨바꼭질.txt")
from collections import deque
# BFS (최소)로 3가지 방향을 거리가 1로 채워지지 않았을 때, 이전보다 +1하고 Q에 추가한다.
# node가 지정된 K일 때, 그 거리값을 구한다. D[K] 이자 D[node]
# for문의 변수는 계속 변해야 하므로 in tuple 내부 변수 주의
def BFS(sn):
    Q =deque([sn])
    while Q:
        n = Q.popleft()
        if n == K:
            return D[n]
        for new in (n-1 , n+1, 2*n):
            if 0 <= new < Inf and D[new] == 0:
                D[new] = D[n] + 1
                Q.append(new)

    return -1

N, K = map(int, input().split())
Inf = 0x19999
D = [0]*Inf
answer = BFS(N)
print(answer)
