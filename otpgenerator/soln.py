def square(i):
    return i*i

t=int(input())
while t:
    num=str(input())
    res = str()
    for i in range(0,len(num)):
        if i%2 == 1:
            res = res + str(square(int(num[i])))
    print(res[:4])
    t=t-1