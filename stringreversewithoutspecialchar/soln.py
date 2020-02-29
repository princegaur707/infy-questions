t=int(input())
while t:
    s = str(input())
    n = len(s)
    arr = list(s)
    new = [0]*n
    for i in range(0,len(arr)):
        if arr[i].isalnum():
            new[n-i-1]=arr[i]
        else:
            new[i-1]=arr[i]
    print(new)
    t=t-1