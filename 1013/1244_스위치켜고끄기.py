import sys;
sys.stdin = open("1244_스위치켜고끄기.txt")

N = int(input())
arr = list(map(int, input().split()))
students = int(input())
for s in range(students):
    sex, num = map(int, input().split())
    num -= 1
    if sex == 1:
        for i in range(num+1, N+1, num+1):
            if not arr[i-1]:
                arr[i-1] = 1
            else:
                arr[i-1] = 0
    elif sex == 2:
        k = 1
        while arr[num-k] == arr[num+k] and num-k >= 0 and num+k < N-1:
            if arr[num-k] == 0 :
                arr[num-k] = arr[num+k] = 1
            else:
                arr[num-k] = arr[num+k] = 0
            k += 1

        if not arr[num]:
            arr[num] = 1
        else:
            arr[num] = 0
for i in range(0, len(arr), 20):
    print(*arr[i:i+20])