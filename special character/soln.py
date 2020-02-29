from itertools import zip_longest
t=int(input())
while t:
    s = str(input())
    even = []
    odd = []
    cntspecialchar = 0
    for i in s:
        if i.isdigit():
            if int(i)%2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))
        elif not(i.isalnum()):
            cntspecialchar+=1
    if cntspecialchar%2 == 0:
        for i,j in zip_longest(even,odd):
            if i != None:
                print(i,end="")
            if j != None:
                print(j,end="")
    else:
        for i,j in zip_longest(odd,even):
            if i!= None:
                print(i,end="")
            if j!= None:
                print(j,end="")
    print()
    t=t-1
