a = list(map(int,input().split()))
b = int(input())
if b not in a:
    print(-1)
    exit(0)
max,ind=a[0],0
i = 1
while i < len(a):
    if a[i]>max:
        max = a[i]
        ind = i-1
    i+=1

print(ind-1)