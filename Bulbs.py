def replce(lst):
    d= {}
    d[0] =1
    d[1] = 0
    for i in range(len(lst)):
        lst[i] = d[lst[i]]
    return lst
lst = list(map(int,input().split()))
switch = 0
for i in range(len(lst)):
    if lst[i] ==1:
        continue
    else:
        switch += 1
        lst = lst[:i]+replce(lst[i:])
print(switch)