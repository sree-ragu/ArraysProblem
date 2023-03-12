lst  = list(map(int,input().split()))
i = len(lst)-1
arr =[lst[i]]
while i>=0:
    if lst[i]>arr[0]:
        arr.insert(0,lst[i])
    i = i-1
print(arr)