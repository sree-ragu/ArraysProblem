for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    b  = int(input())
    print(1 if b in lst else 0)
    