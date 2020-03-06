from itertools import combinations
t=int(input())
while t:
    arr = list(map(int,input().split(',')))
    sm = int(input())
    comblist = combinations(arr,4)
    cnt = 0
    for i in comblist:
        if sum(list(i)) == sm:
            print(list(i))
            cnt = cnt + 1
    print(cnt)
    t=t-1