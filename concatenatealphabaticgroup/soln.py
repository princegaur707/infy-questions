from collections import defaultdict
def listToString(arr):
    return "".join(arr)

t=int(input())
while t:
    d = defaultdict(list)
    s = str(input())
    for i in s:
        d[i.lower()].append(i)
    d = dict(sorted(d.items(),key = lambda x:x[0]))
    res = list(d.values())
    i = 0
    j = len(res)-1
    while i <= j:
        if i==j:
            print(listToString(res[i]),end="")
        else:
            print(listToString(res[i])+""+listToString(res[j]),end="")
        i+=1
        j-=1
    t=t-1