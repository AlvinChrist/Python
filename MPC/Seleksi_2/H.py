size = int(input())
arr = list(map(int,input().split()))
temp = 0
found = False
ind_log = []
sort = True
for x in range(0,size-1):
    if arr[x]<arr[x+1]:
        pass
    else:
        sort=False
        if not found:
            ind_log.append(x+1)
            found=True
        else:
            ind_log.append(x+2)
    
if len(ind_log)==2:
    print("yes")
    print(*ind_log)
elif sort:
    print("yes")
    print("1 1")
else:
    print("no")