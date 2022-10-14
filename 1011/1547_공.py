import sys
sys.stdin = open("1547_공.txt")

inits = 1
tc = input()
for _ in range(int(tc)):
    a, b = map(int, input().split())
    if inits == a:
        inits = b
    elif inits == b:
        inits = a
print(inits)