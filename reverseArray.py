lst = list(map(int,input().split()))
new = []
i = len(lst)-1
while i>=0:
    new.append(lst[i])
    i = i-1
print(new)