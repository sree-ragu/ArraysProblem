a = list(map(int,input().split()))
b =  int(input())
i ,j = 0,len(a)-1
a.sort()
while i<j:
    sum = a[i]+a[j]
    if sum == b:
        print('Pair:',i+1,j+1)
        print(1)
        exit(0)
    if sum >b:
        j = j-1
    else:
        i = i+1
print(0)
    
