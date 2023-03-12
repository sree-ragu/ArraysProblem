
a = list(map(int,input().split()))
minimum,maxmimum = 10**9,-10**9
for i in a:
    if i%2 == 0:
        maxmimum = max(maxmimum,i)
    else:
        minimum = min(minimum,i)
print(maxmimum-minimum)