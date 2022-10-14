import sys
sys.stdin = open("1731_추론.txt")

tc = int(input())
a = int(input())
b = int(input())
c = int(input())

op = []
if c-b == b-a :
    op = ["+",b-a]
elif c//b == b//a:
    op = ["x",c//b]

n = c
for _ in range(tc-3):
    n = int(input())
if op[0] =="+":
    n += op[1]
elif op[0] == "x":
    n *= op[1]
print(n)




