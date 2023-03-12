lst = input().split()
for i in list(map(int,input().split())):
    print(*(lst[i:]+lst[:i]))