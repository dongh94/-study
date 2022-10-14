import sys;
sys.stdin = open("1371_가장많은글자.txt", "r")
inputs = sys.stdin.readline

counts = [0]*26
alpha = []
for i in range(26):
    alpha.append(chr(97+i))
# print(alpha)

for _ in range(50):
    a = inputs()
    for i in a:
        idx = ord(i)-97
        if 0<=idx<=26:
            counts[idx] += 1

max_v = max(counts)
answer = ""
for i in range(len(counts)):
    if counts[i] == max_v:
        answer += alpha[i]
print(answer)


