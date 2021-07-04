umur = list(map(int,input().split()))
i = 0
if(umur[0]<=umur[1]):
    for i in range(0,10000):
        if(umur[0]>umur[1]):
            break
        umur[0]*=3
        umur[1]*=2
print(i)