import sys; sys.stdin = open("1246_모음의개수.txt")
check = ['a','e','i','o','u',"A","E",'I','O','U']
while True:
    a = input()
    if a == "#": break;
    count = 0
    for i in a:
        if i in check:
            count += 1
    print(count)