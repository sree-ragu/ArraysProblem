n = int(input())
lst = list(map(int,input().split()))
b = int(input())
print(' '.join([str(x) for x in (lst[b:]+lst[:b])]))