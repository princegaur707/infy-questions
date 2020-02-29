t=int(input())
while t:
    s = str(input())
    i = 0
    j = len(s) - 1
    cnt = 0
    while i < j :
        if s[i]==s[j]:
            cnt+=1
            i+=1
            j-=1
        else:
            break
    print(cnt)
    t=t-1