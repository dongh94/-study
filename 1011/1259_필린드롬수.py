import sys
sys.stdin = open("1259_팰린드롬수.txt", "r")
while True:
    a = input()
    if a=='0': break;
    answer = "yes"

    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            answer = "no"

    print(answer)


