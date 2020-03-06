import re
t = int(input())
while t:
    s = str(input())
    res = re.sub("\D","",s)
    t=t-1