for _ in range(int(input())):
    n = int(input())
    lst=  list(map(int,input().split()))
    even,odd =[],[]
    for i in lst:
        if i%2:
            odd.append(str(i))
        else:
            even.append(str(i))
    print(*odd)
    print(*even)