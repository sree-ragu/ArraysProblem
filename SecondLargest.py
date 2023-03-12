a = list(map(int,input().split()))
if len(a) == 1:
    print(-1)
    exit(0)
a.sort()
sMax,max= -1,-1
for i in a:
    if i>max:
        sMax = max
        max= i
print(sMax)