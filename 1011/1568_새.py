import sys
sys.stdin = open("1568_새.txt")

a = int(input())
cnt = 0
i = 1
while a > 0:
    if a < i:
        i = 1
    a -= i
    i += 1
    cnt += 1
print(cnt)
