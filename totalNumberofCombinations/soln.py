from itertools import permutations,combinations
t=int(input())
while t:
    arr = list(map(int,input().split(',')))
    k = int(input())
    sm = int(input())
    perlist = combinations(arr,k)
    cnt = 0
    for i in perlist:
        if sum(i) == sm:
            cnt+=1
            print(i)
    print(cnt)
    t=t-1